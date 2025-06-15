import api_key
import boto3
from botocore.config import Config
import hashlib
import logging
import os
import sys
import settings
from datetime import datetime
import utils

# Set up logging
utils.setup_logger()
logger = logging.getLogger(__name__)

# Hardcoded date range for downloads
START_DATE = datetime.strptime(settings.START_DATE, '%Y-%m-%d')
END_DATE = datetime.strptime(settings.END_DATE, '%Y-%m-%d')
logger.info(f"Downloading files from {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")

aws_access_key_id = api_key.read_api_key_id()
aws_secret_access_key = api_key.read_api_key()

def calculate_etag(file_path, chunk_size=8 * 1024 * 1024):
    """Calculate ETag for multipart upload to match S3's calculation"""
    md5s = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            md5s.append(hashlib.md5(chunk).digest())
    if len(md5s) == 1:
        # Single part upload - return simple MD5
        return md5s[0].hex()
    else:
        # Multipart upload - combine MD5s and add part count
        combined_md5 = hashlib.md5(b''.join(md5s)).hexdigest()
        return f"{combined_md5}-{len(md5s)}"

def equal_md5(bucket_name, object_key, local_file_path, s3_client):
    """Verify that local file and the bucket object have the same size and MD5 checksum"""
    logger.info(f"Verifying {local_file_path} against {bucket_name}/{object_key}")
    # Get remote file metadata
    response = s3_client.head_object(Bucket=bucket_name, Key=object_key)
    remote_etag = response['ETag'].strip('"')
    remote_size = response['ContentLength']
    # Check file sizes first (quick check)
    local_size = os.path.getsize(local_file_path)
    if remote_size != local_size:
        logger.warning("✗ File sizes do not match")
        return False
    logger.info("✓ File sizes match")
    chunk_size = 100 * 1024 * 1024
    calculated_etag = calculate_etag(local_file_path, chunk_size)
    if calculated_etag == remote_etag:
        logger.info("✓ Checksums match")
        return True
    logger.warning("✗ Checksum verification failed")
    return False

def download_file(bucket_name, object_key, local_file_path, s3_client):
    # if file already exists, skip download
    if os.path.exists(local_file_path):
        is_valid = equal_md5(bucket_name, object_key, local_file_path, s3_client)
        if is_valid:
            logger.info(f"File {local_file_path} already exists and checksum matches, skipping download.")
            return
    # download the file
    logger.info(f"Downloading {object_key} to {local_file_path}")
    s3_client.download_file(bucket_name, object_key, local_file_path)
    logger.info("Download complete.")

def should_download_file(filename, start_date, end_date):
    """Check if file should be downloaded based on date range"""
    if filename.endswith('.csv.gz'):
        date_part = filename.replace('.csv.gz', '')
        file_date = datetime.strptime(date_part, '%Y-%m-%d')
        if file_date is None:
            logger.warning(f"Warning: Could not extract date from {filename}, skipping")
            return False
    else:
        logger.warning(f"Unexpected filename format: {filename}, expected .csv.gz, skipping")
        return False
    return start_date <= file_date <= end_date

# Initialize a session using your credentials
session = boto3.Session(
  aws_access_key_id,
  aws_secret_access_key,
)
# Create a client with your session and specify the endpoint
s3 = session.client(
  's3',
  endpoint_url='https://files.polygon.io',
  config=Config(signature_version='s3v4'),
)
paginator = s3.get_paginator('list_objects_v2')
prefix = 'us_stocks_sip/trades_v1'
bucket_name = 'flatfiles'
try:
    # List bucket objects using the selected prefix
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page['Contents']:
            object_key = obj['Key']
            object_path_parts = object_key.split('/')
            if not should_download_file(object_path_parts[-1], START_DATE, END_DATE):
                continue
            local_file_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'flatfiles', *object_path_parts[:-1])
            os.makedirs(local_file_dir, exist_ok=True)
            local_file_path = os.path.join(local_file_dir, object_path_parts[-1])
            download_file(bucket_name, object_key, local_file_path, s3)
except KeyboardInterrupt:
    print() # to add a newline after the keyboard interrupt C^
    logger.info("Download interrupted by user.")
    sys.exit(0)
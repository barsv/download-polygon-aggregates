import logging
import sys

def setup_logger():
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            # logging.FileHandler('polygon_download.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
import os
import settings

# Read API key from api_key.txt
def read_api_key(file_path='api_key.txt'):
    """Read API key from api_key.txt."""
    try:
        # if file_path is not absolute
        if not os.path.isabs(file_path):
            file_path = os.path.join(settings.PROJECT_DIR, file_path)
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
        print(f"Successfully read api_key.txt. Key len {len(api_key)}")
        return api_key
    except Exception as e:
        print(f"Error reading API key from {file_path}: {e}")
        return None

def read_api_key_id(file_path='api_key_id.txt'):
    """Read API key from api_key_id.txt."""
    try:
        # if file_path is not absolute
        if not os.path.isabs(file_path):
            file_path = os.path.join(settings.PROJECT_DIR, file_path)
        with open(file_path, 'r') as f:
            api_key_id = f.read().strip()
        print(f"Successfully read api_key_id.txt. Key ID len {len(api_key_id)}")
        return api_key_id
    except Exception as e:
        print(f"Error reading API key ID from {file_path}: {e}")
        return None

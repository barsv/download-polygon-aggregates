# Read API key from api_key.txt
def read_api_key(file_path='api_key.txt'):
    """Read API key from api_key.txt."""
    try:
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
        print("Successfully read API key from api_key.txt")
        return api_key
    except Exception as e:
        print(f"Error reading API key from {file_path}: {e}")
        return None

def read_api_key_id(file_path='api_key_id.txt'):
    """Read API key from api_key_id.txt."""
    try:
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
        print("Successfully read API key from api_key_id.txt")
        return api_key
    except Exception as e:
        print(f"Error reading API key from {file_path}: {e}")
        return None

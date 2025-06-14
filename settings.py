import os

# added '..' because:
# 1) i don't want vscode to look into this huge directory.
# 2) i want to use this common directory in other projects.
DATA_DIR = '../polygon-data'

# Get the directory where settings.py is located
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create absolute path to data directory
ABSOLUTE_DATA_DIR = os.path.join(PROJECT_DIR, DATA_DIR)

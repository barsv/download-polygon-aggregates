from datetime import datetime
import os

# added '..' because:
# 1) i don't want vscode to look into this huge directory.
# 2) i want to use this common directory in other projects.
DATA_DIR = '../polygon-data'

# Get the directory where settings.py is located
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Create absolute path to data directory
ABSOLUTE_DATA_DIR = os.path.join(PROJECT_DIR, DATA_DIR)

# Polygon has data from starting from 2003-09-10
# proof: https://polygon.io/docs/flat-files/stocks/trades/2003/09
START_DATE = "2003-09-10"

END_DATE = datetime.now().strftime('%Y-%m-%d')  # Current date
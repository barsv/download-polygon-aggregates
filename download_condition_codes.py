# this script just downloads ticker types to a csv file.
# see https://polygon.io/docs/rest/stocks/tickers/ticker-types

import pandas as pd
from polygon import RESTClient
from api_key import read_api_key
import os
import settings

# Polygon API client
API_KEY = read_api_key()
client = RESTClient(API_KEY)

output_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'condition-codes')
os.makedirs(output_dir, exist_ok=True)

def save_condition_codes(asset_class):
    conditions = client.list_conditions(
        asset_class=asset_class,
        order="asc",
        limit="1000",
        sort="asset_class",
    )
    output_file = os.path.join(output_dir, f'{asset_class}.csv')
    df = pd.DataFrame(conditions)
    df.to_csv(output_file)
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    asset_classes = ['stocks', 'options', 'crypto', 'fx']
    for asset_class in asset_classes:
        save_condition_codes(asset_class)
    print("All saved.")
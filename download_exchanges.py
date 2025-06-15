# this script just downloads exchanges to a csv file.
# see https://polygon.io/docs/rest/stocks/market-operations/exchanges

import pandas as pd
from polygon import RESTClient
from api_key import read_api_key
import os
import settings

# Polygon API client
API_KEY = read_api_key()

client = RESTClient(API_KEY)

output_dir = os.path.join(settings.ABSOLUTE_DATA_DIR, 'exchanges')
os.makedirs(output_dir, exist_ok=True)

def save_exchanges(asset_class):
    exchanges = client.get_exchanges(
        asset_class=asset_class,
        locale="us"
        )
    output_file = os.path.join(output_dir, f'{asset_class}.csv')
    df = pd.DataFrame(exchanges)
    df.to_csv(output_file)
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    asset_classes = ['stocks', 'options', 'crypto', 'fx']
    for asset_class in asset_classes:
        save_exchanges(asset_class)
    print("All exchanges saved.")
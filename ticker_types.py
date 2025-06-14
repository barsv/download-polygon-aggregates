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

types = client.get_ticker_types(
	asset_class="stocks",
	locale="us"
	)

df = pd.DataFrame(types)
output_file = os.path.join(settings.ABSOLUTE_DATA_DIR, 'tickers', "ticker_types.csv" )
df.to_csv(output_file)
print(f"Ticker types saved to {output_file}")
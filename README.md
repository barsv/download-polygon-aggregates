scripts to download all data from polygon.io.
similar project: https://github.com/shinathan/polygon.io-stock-database

status: work in progress. no hope to finish it.

# installation

1. add api_key.txt
   (optional) add api_key_id.txt - required to download flat files.
2. python -m venv venv
3. pip install -r requirements.txt
4. (optional) make sure that you are ok with settings in the settings.py

# how to use

download_bars.py can be used on its own (no dependencies to run another script first) to download OHLC data for a given list of tickers.

download_exchanges.py, download_ticker_types.py, download_condition_codes.py are optional and likely not needed.

download_trades.py can be used on its own (no dependencies to run another script first) to dump trades in flat files. it compares checksums of local files and objects in the s3 bucket so it's safe to rerun it though it takes a while to calculate checksums for local files. if there is no need to check that local files are not broken then it's better to specify the range to download.

download_tickers_history.py can be used on its own (no dependencies to run another script first). it dumps all tickers for all dates. it's required to run calculate_tickers_renames.py that gets renames for all tickers. note: polygon has [api to get renames](https://polygon.io/docs/rest/stocks/corporate-actions/ticker-events) but... you need to know tickers to ask for.



other scripts in the project root are utils-like.


# update requirements

pip freeze > requirements.txt

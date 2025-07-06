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

download_tickers_history.py can be used on its own (no dependencies to run another script first). it dumps all tickers for all dates. active and inactive. inactive is not needed btw.

save_tickers_first_last_active.py - compresses data downloaded by download_tickers_history.py into a small file with columns 'figi', 'ticker', 'first_active', 'last_active'.

download_ticker_overview.py takes result of save_tickers_first_last_active.py and downloads ticker overview (https://polygon.io/docs/rest/stocks/tickers/ticker-overview) for all tickers. this is needed to get market caps of currently active tickers. because i want to start downloading aggregates for big companies.



other scripts in the project root are utils-like.


# update requirements

pip freeze > requirements.txt

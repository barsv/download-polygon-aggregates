'''
This code processes tickers_history.csv file containing ticker symbol history data and
generates intervals showing when each financial instrument (identified by FIGI)
had different ticker symbols.
'''
import csv
from datetime import datetime, timedelta

INPUT_FILE  = "tickers_history.csv"
OUTPUT_FILE = "ticker_intervals.csv"
# End of the last interval is today
GLOBAL_END = datetime.now().date()

# State dictionary: composite_figi → { "ticker": ticker, "start_date": interval start date }
state = {}

with open(INPUT_FILE, newline='', encoding='utf-8') as fin, \
     open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as fout:

    reader = csv.DictReader(fin)
    writer = csv.writer(fout)
    writer.writerow(["composite_figi", "ticker", "start_date", "end_date"])

    for row in reader:
        figi  = row["composite_figi"]
        if not figi:
            # Skip rows without FIGI
            continue
        ticker= row["ticker"]
        date  = datetime.fromisoformat(row["date"]).date()

        if figi not in state:
            # first time encountering this FIGI
            state[figi] = {"ticker": ticker, "start": date}
        else:
            # if ticker changed - close the old interval
            prev = state[figi]
            if ticker != prev["ticker"]:
                end_date = date - timedelta(days=1)
                writer.writerow([
                    figi,
                    prev["ticker"],
                    prev["start"].isoformat(),
                    end_date.isoformat()
                ])
                # and immediately open a new one
                state[figi] = {"ticker": ticker, "start": date}

    # After reading the entire file, write remaining intervals up to today's date
    for figi, prev in state.items():
        writer.writerow([
            figi,
            prev["ticker"],
            prev["start"].isoformat(),
            GLOBAL_END.isoformat()
        ])

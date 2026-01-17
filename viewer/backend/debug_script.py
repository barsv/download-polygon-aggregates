import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# Adjust path to find settings
sys.path.append('/home/stan/src/download-polygon-aggregates')

from viewer.backend.main_service import get_viewport_data

print("Running test...")
try:
    # 1304053609 = Fri Apr 29 2011 05:06:49 GMT
    # 1304156644 = Sat Apr 30 2011 09:44:04 GMT
    # Width 1225
    df = get_viewport_data("AAPL", 1304053609, 1304156644, 1225)
    print("Success")
    if df is not None:
        print(df.head())
        print(df.tail())
    else:
        print("DF is None")
except Exception:
    import traceback
    traceback.print_exc()

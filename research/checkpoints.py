import pickle
import os, glob
from datetime import datetime, timezone
import numpy as np

import pickle
import gzip
import os, glob
from datetime import datetime, timezone
import numpy as np

CKPT = "./data"
os.makedirs(CKPT, exist_ok=True)

def save_ckpt(checkpoint_data, compress=True):
    """Atomic single-file pickle checkpoint with optional compression."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    ext = ".pkl.gz" if compress else ".pkl"
    fp = os.path.join(CKPT, f"ckpt_{ts}{ext}")
    tmp = fp + ".tmp"
    
    if compress:
        with gzip.open(tmp, 'wb') as f:
            pickle.dump(checkpoint_data, f)
    else:
        with open(tmp, 'wb') as f:
            pickle.dump(checkpoint_data, f)
    
    os.replace(tmp, fp)

def load_ckpt():
    """Return checkpoint data from latest checkpoint or None."""
    # Look for both compressed and uncompressed files
    files = sorted(glob.glob(os.path.join(CKPT, "ckpt_*.pkl*")))
    if not files: 
        return None
    
    latest_file = files[-1]
    
    if latest_file.endswith('.gz'):
        with gzip.open(latest_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
    else:
        with open(latest_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
    
    return checkpoint_data

# results1 = [1,2,3]
# results2 = np.zeros(4)
# results2[1] = 123

# save_ckpt({ 'results1': results1, 'results2': results2, 'step': 42, 'test': 'some str'  })

# ckpt = load_ckpt()
# print(ckpt['results1'])
# print(ckpt['results2'])
# print(ckpt['step'])
# print(ckpt['test'])
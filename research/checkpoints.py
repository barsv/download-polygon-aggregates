import pickle
import os, glob
from datetime import datetime, timezone
import numpy as np

import pickle
import gzip
import os, glob
from datetime import datetime, timezone
import numpy as np


def save_ckpt(checkpoint_data, dir, compress=True, max_checkpoints=5):
    """Atomic single-file pickle checkpoint with optional compression."""
    if not dir:
        raise Exception("checkpoint dir is missing")
    os.makedirs(dir, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    ext = ".pkl.gz" if compress else ".pkl"
    fp = os.path.join(dir, f"ckpt_{ts}{ext}")
    tmp = fp + ".tmp"
    
    if compress:
        with gzip.open(tmp, 'wb') as f:
            pickle.dump(checkpoint_data, f)
    else:
        with open(tmp, 'wb') as f:
            pickle.dump(checkpoint_data, f)
    
    os.replace(tmp, fp)
    
    # Clean up old checkpoints, keep only the most recent max_checkpoints
    files = sorted(glob.glob(os.path.join(dir, "ckpt_*.pkl*")))
    if len(files) > max_checkpoints:
        # Remove oldest files
        for old_file in files[:-max_checkpoints]:
            try:
                os.remove(old_file)
            except OSError:
                pass  # Ignore if file was already removed

def load_ckpt(dir, filename=None):
    """Return checkpoint data from latest checkpoint or None."""
    if filename == None:
        # Look for both compressed and uncompressed files
        files = sorted(glob.glob(os.path.join(dir, "ckpt_*.pkl*")))
        if not files: 
            return None
        
        latest_file = files[-1]
    else:
        latest_file = os.path.join(dir, filename)
    
    if latest_file.endswith('.gz'):
        with gzip.open(latest_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
    else:
        with open(latest_file, 'rb') as f:
            checkpoint_data = pickle.load(f)
    
    return checkpoint_data

if __name__ == '__main__':
    print('ok')
    results1 = [1,2,3]
    results2 = np.zeros(4)
    results2[1] = 123
    ckpt_data = { 'results1': results1, 'results2': results2, 'step': 42, 'test': 'some str'  }
    # path to the current script
    pwd = os.path.dirname(os.path.abspath(__file__))
    test_dir = f'{pwd}/data/ckpt_test'
    save_ckpt(ckpt_data, test_dir)

    ckpt = load_ckpt(test_dir)
    print(ckpt['results1'])
    print(ckpt['results2'])
    print(ckpt['step'])
    print(ckpt['test'])
This folder contains exploratory notebooks and prototypes used to understand Polygon data and test ideas.

Jupytext Pairing
- Pairing: notebooks are paired with `py:percent` scripts into `research/pyfiles/` (see `research/.jupytext.toml`).
- Install: `pip install jupytext` (add to your venv).
- Sync both ways:
  - One-shot: `jupytext --sync research/<notebook>.ipynb`
  - All notebooks: `bash tools/jupytext_sync.sh`

Workflow Tips
- Review in diffs: commit the paired `.py` to get readable reviews in PRs.
- Edit anywhere: you can change either the `.ipynb` in Jupyter or the `.py` in an editor; run sync to update the pair.
- Data paths: notebooks assume data under `../polygon-data/` as defined in `settings.py`.

Git policy
- Paired `.py` files are generated into `research/pyfiles/` and are ignored by Git by default.

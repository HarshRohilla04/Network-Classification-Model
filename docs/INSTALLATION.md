
# Installation Instructions

1. Install Python 3.10+.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Prepare data in `./data/` (not committed). Expected CSV schema:
   - Columns: features listed in `configs/default.yaml` plus `label`

4. Update `./configs/default.yaml` paths if needed.


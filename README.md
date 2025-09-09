# vigil
real time log and video analyser

# fresh clone
git clone https://github.com/<org-or-user>/vigil-logwatch.git
cd vigil-logwatch
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt

# (if needed) generate sample data
python scripts/generate_sample_logs.py --out assets/sample_logs.csv --rows 6000 --interval 100ms

# run the app
python src/main.py

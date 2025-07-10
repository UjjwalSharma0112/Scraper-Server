# Clone your repo

git clone https://github.com/yourusername/scraper-server.git
cd scraper-server

# Create and activate venv

python3 -m venv .venv
source .venv/bin/activate

# Install all packages

pip install -r requirements.txt

# Run the FastAPI app

uvicorn server:app --host 0.0.0.0 --port 8000

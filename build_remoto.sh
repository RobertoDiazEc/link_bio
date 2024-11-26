cd link_bio
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://api.cpkm.com.co reflex export --frontend-only
unzip frontend.zip -d public
rm -f  frontend.zip
deactivate
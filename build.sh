source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
API_URL=https://api.cpkm.com.co reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f  frontend.zip
deactivate
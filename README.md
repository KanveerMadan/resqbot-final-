# FastAPI Model Deployment on Render

## How to Deploy

1. Push this repo to GitHub.
2. Go to https://render.com and create a new Web Service.
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - Python Version: from runtime.txt
4. Add `combined_model.pkl` to the repo before pushing.
# 小一小二华文测验 — Streamlit app

Primary 1–2 Chinese dictation (听写) and understanding test.

## Files
- `streamlit_app.py` — the Streamlit entry point
- `huawen_test.html` — the test itself (dictation pad, quiz, revise list, school list)
- `requirements.txt`

## Run on your computer
```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud (free)
1. Create a new **public** GitHub repository and upload these three files to it.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app** → **Deploy a public app from GitHub**.
4. Pick your repository, branch `main`, main file `streamlit_app.py`, then **Deploy**.
5. After a minute or two you get a link like `https://<your-name>-huawen.streamlit.app` to open on any phone, tablet or computer.

To change the word bank, edit the `RAW` list near the bottom of `huawen_test.html` and push the change; the app redeploys on its own.

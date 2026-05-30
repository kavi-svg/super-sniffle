# Chatbot (Alex)

This is a small rule-based chatbot using NLTK and a minimal Flask web UI.

Run locally

1. Install dependencies:

```powershell
cd "C:\Users\hp\OneDrive\Documents\expert_system_app.py\Chatbot.py"
py -m pip install -r web\requirements.txt
```

2. Start the web UI:

```powershell
py -m web.app
```

Open http://127.0.0.1:5000 in your browser.

Run console bot:

```powershell
py .\chatbot.py
```

How to push to GitHub

1. Create a repo on GitHub and copy its URL (e.g. `https://github.com/youruser/yourrepo.git`).
2. From this folder run:

```bash
git init
git add .
git commit -m "Add chatbot and web UI"
git branch -M main
git remote add origin https://github.com/youruser/yourrepo.git
git push -u origin main
```

If you want, share the GitHub repo URL and I can push for you.

# How to run

### 1. Install all required packages
```bash
pip install -r requirements.txt
```
### 2. Run recognition server
```bash
python3 -m uvicorn server.server:app --reload
```
### 3. Run recognition client
```bash
python3 tg_bot/bot.py
```
    
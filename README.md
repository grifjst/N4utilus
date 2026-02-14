![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-teal)
![License](https://img.shields.io/badge/License-MIT-green)

# N4utilus

N4utilus is a Python-based cryptographic bot detection service built with **FastAPI**.  
It uses a **challenge–response mechanism** (nonce + HMAC-SHA256) to help distinguish legitimate users from automated bots.

---

## What this project demonstrates

- Secure challenge–response authentication design
- HMAC-based message verification
- Replay attack prevention using one-time nonces
- REST API design with FastAPI
- Client/server interaction testing

---

## How it works

1. Server issues a one-time cryptographic nonce  
2. Client signs the nonce using HMAC-SHA256  
3. Server verifies the signature  
4. Nonces are consumed to prevent replay attacks  

---

## Requirements

- Python 3.10+
- Windows, macOS, or Linux

---

## Setup (Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

## Demo

Start the server by running the following command in your terminal:

python -m uvicorn server:app --reload

Once running, the server will be available at:
http://127.0.0.1:8000

To request a challenge nonce, open your browser and visit:
http://127.0.0.1:8000/challenge

You should receive a JSON response similar to:
{"nonce":"<random_value>"}

With the server still running, open a second terminal and run the client:
python client.py

If the verification succeeds, the expected output is:
Status: 200
Response: {'ok': True, 'verdict': 'likely-legit-client'}

Interactive API documentation is available at:
http://127.0.0.1:8000/docs

Security notes:
- Secret keys are hardcoded for demo purposes only
- Environment variables should be used in production
- In-memory nonce storage is not suitable for distributed systems



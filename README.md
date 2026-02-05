# N4utilus 

N4utilus is a Python based cryptographic bot detector built with FastAPI.
It uses a challenge response mechanism (nonce + HMAC-SHA256) to help
distinguish legitimate clients from automated bots.

## How it works
1. Server issues a one-time nonce
2. Client signs the nonce using HMAC-SHA256
3. Server verifies the signature
4. Nonces are consumed to prevent replay attacks

## Requirements
- Python 3.10+
- Windows, macOS, or Linux

## Setup (Windows)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

## How to run

### Start the server
```powershell
python -m uvicorn server:app --reload

import hmac
import hashlib
import secrets
import time
from fastapi import FastAPI, HTTPException

app = FastAPI(title="N4utilus Bot Detector")

SHARED_SECRET = b"change-this-secret"
NONCES = {}
NONCE_TTL_SECONDS = 60

def now():
    return int(time.time())

def cleanup_nonces():
    t = now()
    for n, exp in list(NONCES.items()):
        if exp <= t:
            NONCES.pop(n, None)

@app.get("/challenge")
def get_challenge():
    cleanup_nonces()
    nonce = secrets.token_urlsafe(24)
    NONCES[nonce] = now() + NONCE_TTL_SECONDS
    return {"nonce": nonce, "expires_in": NONCE_TTL_SECONDS}

@app.post("/verify")
def verify(payload: dict):
    cleanup_nonces()

    nonce = payload.get("nonce")
    signature = payload.get("signature")

    if not nonce or not signature:
        raise HTTPException(400, "Missing nonce or signature")

    if nonce not in NONCES:
        raise HTTPException(401, "Invalid or expired nonce")

    NONCES.pop(nonce, None)

    expected = hmac.new(
        SHARED_SECRET,
        nonce.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected, signature):
        raise HTTPException(401, "Signature mismatch (likely bot)")

    return {"ok": True, "verdict": "likely-legit-client"}

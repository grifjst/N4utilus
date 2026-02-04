import requests
import hmac
import hashlib

BASE = "http://127.0.0.1:8000"
SHARED_SECRET = b"change-this-secret"

resp = requests.get(f"{BASE}/challenge")
resp.raise_for_status()
nonce = resp.json()["nonce"]

signature = hmac.new(
    SHARED_SECRET,
    nonce.encode(),
    hashlib.sha256
).hexdigest()

verify = requests.post(
    f"{BASE}/verify",
    json={"nonce": nonce, "signature": signature}
)

print("Status:", verify.status_code)
print("Response:", verify.json())

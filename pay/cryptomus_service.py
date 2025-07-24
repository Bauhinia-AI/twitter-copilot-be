# cryptomus_service.py

import json
import hmac
import hashlib
import requests
from config import CRYPTOMUS_API_KEY, CRYPTOMUS_MERCHANT_ID, CRYPTOMUS_BASE_URL


def generate_sign(data: dict) -> str:
    raw = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    return hmac.new(CRYPTOMUS_API_KEY.encode(), raw.encode(), hashlib.sha256).hexdigest()


def create_invoice(data: dict) -> dict:
    headers = {
        "merchant": CRYPTOMUS_MERCHANT_ID,
        "sign": generate_sign(data),
        "Content-Type": "application/json"
    }
    response = requests.post(CRYPTOMUS_BASE_URL, json=data, headers=headers)
    return response.json()


def verify_callback_signature(raw_body: str, signature: str) -> bool:
    expected = hmac.new(CRYPTOMUS_API_KEY.encode(), raw_body.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

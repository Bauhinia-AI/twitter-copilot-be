import os
from dotenv import load_dotenv

load_dotenv()


# Cryptomus
CRYPTOMUS_API_KEY = os.getenv("CRYPTOMUS_API_KEY")
CRYPTOMUS_MERCHANT_ID = os.getenv("CRYPTOMUS_MERCHANT_ID")
CRYPTOMUS_BASE_URL = "https://api.cryptomus.com/v1/payment"
CALLBACK_SECRET = CRYPTOMUS_API_KEY  # 签名验证用同一个密钥
CALLBACK_URL = "https://api.agenticgui.ai/cryptomus_callback"
RETURN_URL = "https://api.agenticgui.ai/success"
# schemas.py

from pydantic import BaseModel
from typing import Optional


class PaymentRequest(BaseModel):
    amount: float
    currency: str = "USDT"
    order_id: str
    network: str = "TRC20"


class CryptomusCallback(BaseModel):
    uuid: str
    order_id: str
    status: str
    amount: str
    currency: str
    payer_amount: Optional[str] = None
    payer_currency: Optional[str] = None
    hash: Optional[str] = None

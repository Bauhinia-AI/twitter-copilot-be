from fastapi import APIRouter, Request, Header, HTTPException
from fastapi.responses import JSONResponse
import json
import logging
from .cryptomus_service import create_invoice, verify_callback_signature
from .schema import PaymentRequest
from config import CALLBACK_URL, RETURN_URL

# 创建路由器
router = APIRouter(prefix="/pay", tags=["payment"])

# 获取logger
logger = logging.getLogger(__name__)

@router.post("/create_payment")
async def create_payment(payload: PaymentRequest):
    """创建支付订单"""
    invoice_data = {
        "amount": str(payload.amount),
        "currency": payload.currency,
        "order_id": payload.order_id,
        "network": payload.network,
        "url_callback": CALLBACK_URL,
        "url_return": RETURN_URL,
        "lifetime": 900
    }
    response = create_invoice(invoice_data)
    return JSONResponse(content=response)


@router.post("/cryptomus_callback")
async def cryptomus_callback(request: Request, sign: str = Header(None)):
    """处理Cryptomus回调"""
    raw_body = await request.body()
    raw_text = raw_body.decode()

    if not verify_callback_signature(raw_text, sign):
        raise HTTPException(status_code=403, detail="Invalid signature")

    payload = json.loads(raw_text)
    logger.info(f"Cryptomus callback payload: {payload}")
    status = payload.get("status")
    order_id = payload.get("order_id")

    if status == "paid":
        logger.info(f"✅ 订单 {order_id} 支付成功")
        # TODO: 更新数据库、发货等

    return {"status": "ok"} 
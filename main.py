# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

# 导入路由模块
from pay.router import router as pay_router

import logging
import os
from logging.handlers import TimedRotatingFileHandler

# 日志配置
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "twitter_copilot.log")

file_handler = TimedRotatingFileHandler(
    log_file, when="midnight", interval=1, backupCount=7, encoding="utf-8"
)
file_handler.suffix = "%Y-%m-%d"

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)
file_handler.setFormatter(formatter)

# Console output
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    handlers=[file_handler, stream_handler]
)

# 创建FastAPI应用
app = FastAPI(
    title="Twitter Copilot Backend",
    description="Twitter Copilot Backend",
    version="1.0.0"
)

# 注册路由
app.include_router(pay_router)

@app.get("/")
async def root():
    """根路径 - 健康检查"""
    return JSONResponse(content={"message": "Twitter Copilot Backend is running", "status": "healthy"})

@app.get("/health")
async def health_check():
    """健康检查端点"""
    return JSONResponse(content={"status": "healthy", "service": "twitter-copilot-backend"})

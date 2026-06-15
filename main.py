import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv

# تنظیم اولیه
load_dotenv()

# تنظیمات لاگ (در Render مفید است)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# تعریف Lifespan برای مدیریت چرخه حیات FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    """در اینجا کارهای شروع و پایان را انجام می‌دهیم (مثلاً تنظیم webhook)"""
    logger.info("Application startup")
    # بعداً بات را راه‌اندازی می‌کنیم
    yield
    logger.info("Application shutdown")

# ساخت اپلیکیشن FastAPI
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    """تلگرام پیام‌ها را به این مسیر POST می‌کند."""
    # فعلاً فقط داده را می‌خوانیم
    data = await request.json()
    logger.info(f"Received update: {data}")
    # بعداً اینجا منطق بات قرار می‌گیرد
    return Response(status_code=200)
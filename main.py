import os
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application

# هندلرهای ربات را از پکیج bot وارد می‌کنیم
from bot.handlers import setup_handlers

# بارگذاری متغیرهای محیطی
load_dotenv()

# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# تعریف lifespan برای مدیریت چرخه حیات FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    """ایجاد Application ربات، تنظیم و پاک‌سازی webhook"""
    # توکن و آدرس webhook از env
    bot_token = os.getenv("BOT_TOKEN")
    webhook_url = os.getenv("WEBHOOK_URL")
    if not bot_token or not webhook_url:
        raise ValueError("BOT_TOKEN and WEBHOOK_URL must be set")

    # ساخت Application ربات
    application = Application.builder().token(bot_token).build()

    # اضافه کردن هندلرها
    setup_handlers(application)

    # ذخیره application در state برنامه FastAPI (برای دسترسی در endpoint)
    app.state.telegram_app = application

    # تنظیم webhook هنگام شروع
    await application.bot.set_webhook(url=webhook_url)
    logger.info(f"Webhook set to {webhook_url}")

    # شروع Application (برای job_queue و ...)
    await application.initialize()
    await application.start()

    yield   # <--- سرور در اینجا اجرا می‌شود

    # عملیات هنگام shutdown
    logger.info("Shutting down bot")
    await application.stop()
    await application.shutdown()
    await application.bot.delete_webhook()
    logger.info("Webhook removed")

# ساخت اپلیکیشن FastAPI با lifespan
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/webhook")
async def webhook(request: Request):
    """تلگرام آپدیت‌ها را به اینجا POST می‌کند."""
    data = await request.json()
    update = Update.de_json(data, app.state.telegram_app.bot)
    # پردازش آپدیت به صورت async
    await app.state.telegram_app.process_update(update)
    return Response(status_code=200)
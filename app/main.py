from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from telegram import Update

from app.bot.application import telegram_app
from app.bot.webhook import set_webhook


@asynccontextmanager
async def lifespan(app: FastAPI):

    await telegram_app.initialize()

    await set_webhook()

    yield

    await telegram_app.shutdown()


app = FastAPI(
    title="YouTube Subtitle Bot",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "status": "ok"
    }


@app.post("/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    update = Update.de_json(
        data,
        telegram_app.bot
    )

    await telegram_app.process_update(update)

    return {
        "status": "ok"
    }
from fastapi import FastAPI, Request

from telegram import Update

from app.bot.application import telegram_app


app = FastAPI(
    title="YouTube Subtitle Bot"
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
from fastapi import FastAPI
from app.bot.application import telegram_app

app = FastAPI(
    title="YouTube Subtitle Bot"
)

@app.get("/")
async def root():
    return {
        "status": "ok"
    }
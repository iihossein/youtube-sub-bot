from app.bot.application import telegram_app
from app.config import WEBHOOK_URL


async def set_webhook():

    await telegram_app.bot.set_webhook(
        WEBHOOK_URL
    )
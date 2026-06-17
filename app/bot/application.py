from telegram.ext import (
    Application,
    CommandHandler
)

from app.config import BOT_TOKEN
from app.bot.handlers import start_command


telegram_app = (
    Application.builder()
    .token(BOT_TOKEN)
    .build()
)

telegram_app.add_handler(
    CommandHandler(
        "start",
        start_command
    )
)
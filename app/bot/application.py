from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from app.config import BOT_TOKEN
from app.bot.handlers import start_command
from app.bot.handlers import message_handler


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

telegram_app.add_handler(
    MessageHandler(
        filters.Text & ~filters.COMMAND,
        message_handler
    )
)

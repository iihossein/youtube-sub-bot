from telegram import Update
from telegram.ext import ContextTypes


async def start_command( update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n\nلینک ویدیوی یوتیوب را ارسال کنید."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    
    await update.message.reply_text(
        f"لینک دریافت شد:\n{text}"
    )
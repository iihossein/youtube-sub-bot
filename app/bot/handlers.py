from telegram import Update
from telegram.ext import ContextTypes
from app.services.youtube_service import YouTubeService


async def start_command( update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n\nلینک ویدیوی یوتیوب را ارسال کنید."
    )


async def message_handler(update, context):

    url = update.message.text

    try:

        video_info = (
            YouTubeService
            .get_video_info(url)
        )

        title = video_info.get(
            "title",
            "Unknown"
        )

        duration = video_info.get(
            "duration",
            0
        )

        await update.message.reply_text(
            f"🎬 {title}\n⏱ {duration} ثانیه"
        )

    except Exception as error:

        await update.message.reply_text(
            f"خطا:\n{error}"
        )
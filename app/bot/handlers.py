from telegram import Update
from telegram.ext import ContextTypes
from app.services.youtube_service import YouTubeService

from app.utils.youtube import extract_video_id



async def start_command( update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n\nلینک ویدیوی یوتیوب را ارسال کنید."
    )


async def message_handler(
    update,
    context
):

    try:

        url = update.message.text

        video_id = (
            extract_video_id(url)
        )

        transcript = (
            YouTubeService
            .get_farsi_subtitle(
                video_id
            )
        )

        count = len(transcript)

        await update.message.reply_text(
            f"زیرنویس پیدا شد ✅\n"
            f"تعداد خطوط: {count}"
        )

    except Exception as error:

        await update.message.reply_text(
            f"خطا:\n{error}"
        )
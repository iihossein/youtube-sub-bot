from dotenv import load_dotenv
import os

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

MAX_VIDEO_DURATION = int(
    os.getenv("MAX_VIDEO_DURATION", 3600)
)
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# تعریف handler های async

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """پاسخ به دستور /start"""
    await update.message.reply_text(
        "سلام! 👋\n"
        "من ربات دانلود زیرنویس فارسی یوتیوب هستم.\n"
        "کافیه لینک ویدیو یوتیوب رو برام بفرستی تا زیرنویس فارسی رو (اگر موجود باشه) واست بفرستم.\n"
        "اگر زیرنویس فارسی نباشه، زیرنویس انگلیسی رو ترجمه می‌کنم.\n"
        "فعلاً در نسخه آزمایشی، فقط لینک رو برمی‌گردونم. 😅"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """پاسخ به پیام‌های متنی (فعلاً فقط لینک‌ها را echo می‌کنیم)"""
    text = update.message.text.strip()
    # بررسی ساده که حاوی youtube باشد
    if "youtube.com" in text or "youtu.be" in text:
        await update.message.reply_text(f"🔗 لینک یوتیوب دریافت شد:\n{text}\n\n(پردازش در آینده...)")
    else:
        await update.message.reply_text("لطفاً یک لینک معتبر یوتیوب بفرستید.")

def setup_handlers(application: Application):
    """رجیستر کردن همه هندلرها در Application"""
    # دستور /start
    application.add_handler(CommandHandler("start", start))
    # هر پیام متنی دیگر (به‌جز دستورات)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
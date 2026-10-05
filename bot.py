from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Yahan apna bot token daalein (BotFather se milega)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Aapka channel username (bina @ ke)
CHANNEL_USERNAME = "nr_hackz"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name

    # Inline button banayein
    keyboard = [
        [
            InlineKeyboardButton(
                text="🚀 Join NR_HACKZ Channel",
                url=f"https://t.me/{CHANNEL_USERNAME}"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message bhejein button ke saath
    await update.message.reply_text(
        f"👋 Hello {user_name}!\n\n"
        f"Welcome! Neeche diye gaye button par click karke hamara channel join karein 👇",
        reply_markup=reply_markup
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot chal raha hai...")
    app.run_polling()


if __name__ == "__main__":
    main()

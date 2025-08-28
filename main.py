import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("¡Hola! Soy tu bot de Telegram 🚀")

def main():
    # 🔑 Leemos el token desde la variable de entorno BOT_TOKEN
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("No se encontró la variable de entorno BOT_TOKEN")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

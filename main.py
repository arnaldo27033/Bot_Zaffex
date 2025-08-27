from telegram.ext import Updater, CommandHandler

# Token de tu bot
TOKEN = "8237505672:AAEwkUJwpKAgqVdrIQbbfWH6UZwHbNsNO5k"

# Comando /start
def start(update, context):
    update.message.reply_text("¡Hola! Soy tu bot en Render 😎")

# Comando /help
def help_command(update, context):
    update.message.reply_text("Comandos disponibles:\n/start - Iniciar el bot\n/help - Mostrar ayuda")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

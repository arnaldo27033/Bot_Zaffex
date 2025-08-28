import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Activa logs para depuración
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Comandos del bot ---
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy tu bot, ya estoy funcionando 🚀")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Comandos disponibles:\n/start - Inicia el bot\n/help - Ayuda")

# --- MAIN ---
def main():
    # Tu token de Telegram
    TOKEN = "8237505672:AAEwkUJwpKAgqVdrIQbbfWH6UZwHbNsNO5k"

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Añadir comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Iniciar bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

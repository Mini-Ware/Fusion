import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#commands
def start(update: Bot, context: CallbackContext) -> None:
    update.message.reply_text("Hello!")

def ping(update: Bot, context: CallbackContext) -> None:
    update.message.reply_text("pong")

def main():
    client = Updater(os.getenv("TOKEN"))
    dispatcher = client.dispatcher

    #handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ping", ping))

    client.start_polling()
    client.idle()

if __name__ == '__main__':
    main()

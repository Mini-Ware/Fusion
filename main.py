import os
import requests
import telegram
from telegram import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#server
import keep_alive
keep_alive.keep_alive()

#commands
def help(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("<strong>Fusion</strong>\nGeneral purpose Telegram bot where you can search for many things\n\n/help  List all avaliable commands\n/id  Retrive chat_id\n/ping  Check response\n/cat  Find a cat image\n/dog  Find a dog image\n\nt.me/fused_bot", parse_mode=telegram.ParseMode.HTML)

def start(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("Hello! You can find the list of avaliable commands using /help")

def ping(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("pong")

def id(update: bot, context: CallbackContext) -> None:
    update.message.reply_text(update.message.chat_id)

def cat(update: bot, context: CallbackContext) -> None:
    json = requests.get(url="https://some-random-api.ml/animal/cat").json()
    context.bot.send_photo(chat_id=update.message.chat_id, photo=json["image"])

def dog(update: bot, context: CallbackContext) -> None:
    json = requests.get(url="https://some-random-api.ml/animal/dog").json()
    context.bot.send_photo(chat_id=update.message.chat_id, photo=json["image"])

def main():
    client = Updater(os.getenv("TOKEN"))
    dispatcher = client.dispatcher

    #handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("ping", ping))
    dispatcher.add_handler(CommandHandler("cat", cat))
    dispatcher.add_handler(CommandHandler("dog", dog))
    dispatcher.add_handler(CommandHandler("id", id))

    client.start_polling()
    client.idle()

if __name__ == '__main__':
    main()

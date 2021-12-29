import os
import requests
import telegram
from telegram import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#server
from keep_alive import keep_alive
keep_alive()

#commands
def help(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("<strong>Fusion</strong>\nGeneral purpose Telegram bot where you can search for many things\n\n/help  List all commands\n/id  Retrive chat_id\n/ping  Check response\n\n🐶 Animals\n/cat  Find a cat image\n/dog  Find a dog image\n\n📊 Statistics\n/covid Get SG covid data\n/weather Get SG weather data\n\nt.me/fused_bot", parse_mode=telegram.ParseMode.HTML)

def start(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("Hello! You can find the list of avaliable commands using /help")

def ping(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("pong")

def id(update: bot, context: CallbackContext) -> None:
    update.message.reply_text("<code>"+str(update.message.chat_id)+"</code>", parse_mode=telegram.ParseMode.HTML)

def weather(update: bot, context: CallbackContext) -> None:

    #cool emotes
    def indicate(here):
      sky = here.lower()
      if sky.find("thunder") != -1:
        return "⛈️ "+here
      elif sky.find("shower") != -1 or sky.find("rain") != -1:
        return "🌧️ "+here
      elif sky.find("clear") != -1 or sky.find("sunny") != -1:
        return "🌤️ "+here
      elif sky.find("cloud") != -1:
        return "☁️ "+here
      elif sky.find("wind") != -1:
        return "💨 "+here
      else:
        return sky

    condition =requests.get('https://api.data.gov.sg/v1/environment/24-hour-weather-forecast').json()
    data = condition["items"][0]
    update.message.reply_text("<strong>24-hour weather forecast</strong>\n\n🌡️ Temperature: "+str(data["general"]["temperature"]["low"])+"-"+str(data["general"]["temperature"]["high"])+"°C\n💧 Humidity: "+str(data["general"]["relative_humidity"]["low"])+"-"+str(data["general"]["relative_humidity"]["high"])+"%\n💨 Wind: "+data["general"]["wind"]["direction"]+" "+str(data["general"]["wind"]["speed"]["low"])+"-"+str(data["general"]["wind"]["speed"]["high"])+"km/h\n\nRegion: North\n"+indicate(data["periods"][0]["regions"]["north"])+" > "+indicate(data["periods"][1]["regions"]["north"])+" > "+indicate(data["periods"][2]["regions"]["north"])+"\n\nRegion: South\n"+indicate(data["periods"][0]["regions"]["south"])+" > "+indicate(data["periods"][1]["regions"]["south"])+" > "+indicate(data["periods"][2]["regions"]["south"])+"\n\nRegion: Central\n"+indicate(data["periods"][0]["regions"]["central"])+" > "+indicate(data["periods"][1]["regions"]["central"])+" > "+indicate(data["periods"][2]["regions"]["central"])+"\n\nRegion: East\n"+indicate(data["periods"][0]["regions"]["east"])+" > "+indicate(data["periods"][1]["regions"]["east"])+" > "+indicate(data["periods"][2]["regions"]["east"])+"\n\nRegion: West\n"+indicate(data["periods"][0]["regions"]["west"])+" > "+indicate(data["periods"][1]["regions"]["west"])+" > "+indicate(data["periods"][2]["regions"]["west"])+"\n\nSource: data.gov.sg", parse_mode=telegram.ParseMode.HTML)


def covid(update: bot, context: CallbackContext) -> None:
    cases =requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=60b1a923-1a5e-44ef-a4ae-046345146725').json()
    data = cases['result']['records']

    x = slice(10)
    y = slice(10, 20)
  
    #80+
    a_unvax = round(float(data[8]['unvaccinated'])/5)
    a_pvax = round(float(data[8]['partially_vaccinated'])/5)
    a_fvax = round(float(data[8]['fully_vaccinated'])/5)

    display_a_unvax = "🟥"*a_unvax
    display_a_pvax = "🟧"*a_pvax
    display_a_fvax = "🟫"*a_fvax
    a_empty = "⬛"*(20-(a_unvax+a_pvax+a_fvax))

    a_chart = display_a_unvax+display_a_pvax+display_a_fvax+a_empty

    a_chart = "Age group: "+data[8]['age']+"\n"+a_chart[x]+"\n"+a_chart[y]

    #70-79
    b_unvax = round(float(data[7]['unvaccinated'])/5)
    b_pvax = round(float(data[7]['partially_vaccinated'])/5)
    b_fvax = round(float(data[7]['fully_vaccinated'])/5)

    display_b_unvax = "🟥"*b_unvax
    display_b_pvax = "🟧"*b_pvax
    display_b_fvax = "🟫"*b_fvax
    b_empty = "⬛"*(20-(b_unvax+b_pvax+b_fvax))

    b_chart = display_b_unvax+display_b_pvax+display_b_fvax+b_empty

    b_chart = "Age group: "+data[7]['age']+"\n"+b_chart[x]+"\n"+b_chart[y]

    #60-69
    c_unvax = round(float(data[6]['unvaccinated'])/5)
    c_pvax = round(float(data[6]['partially_vaccinated'])/5)
    c_fvax = round(float(data[6]['fully_vaccinated'])/5)

    display_c_unvax = "🟥"*c_unvax
    display_c_pvax = "🟧"*c_pvax
    display_c_fvax = "🟫"*c_fvax
    c_empty = "⬛"*(20-(c_unvax+c_pvax+c_fvax))

    c_chart = display_c_unvax+display_c_pvax+display_c_fvax+c_empty

    c_chart = "Age group: "+data[6]['age']+"\n"+c_chart[x]+"\n"+c_chart[y]

    #50-59
    d_unvax = round(float(data[5]['unvaccinated'])/5)
    d_pvax = round(float(data[5]['partially_vaccinated'])/5)
    d_fvax = round(float(data[5]['fully_vaccinated'])/5)

    display_d_unvax = "🟥"*d_unvax
    display_d_pvax = "🟧"*d_pvax
    display_d_fvax = "🟫"*d_fvax
    d_empty = "⬛"*(20-(d_unvax+d_pvax+d_fvax))

    d_chart = display_d_unvax+display_d_pvax+display_d_fvax+d_empty

    d_chart = "Age group: "+data[5]['age']+"\n"+d_chart[x]+"\n"+d_chart[y]

    update.message.reply_text("<strong>Proportion of cases who ever required O2, in ICU or died</strong>\n\n"+a_chart+"\n\n"+b_chart+"\n\n"+c_chart+"\n\n"+d_chart+"\n\nLegend:\n🟥 Unvaccinated\n🟧 Partially Vaccinated\n🟫 Fully Vaccinated\n\nSource: data.gov.sg", parse_mode=telegram.ParseMode.HTML)

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
    dispatcher.add_handler(CommandHandler("covid", covid))
    dispatcher.add_handler(CommandHandler("weather", weather))

    client.start_polling()
    client.idle()

if __name__ == '__main__':
    main()

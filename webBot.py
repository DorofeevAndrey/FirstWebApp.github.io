import telebot
from telebot import types
import BotToken


bot = telebot.TeleBot(BotToken.token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webAppURL = types.WebAppInfo("https://itproger.com")
    webButton = types.KeyboardButton(text='Веб-приложение', web_app=webAppURL)
    keyboard.add(webButton)
    bot.send_message(message.chat.id, 'Открой сайт', reply_markup=keyboard)

bot.polling(True)


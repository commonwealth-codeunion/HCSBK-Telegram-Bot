import telebot
from telebot import types
import requests

linkval = 'https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40'

data = requests.get(linkval)
slovar = data.json()
valuty = slovar['rates']


token = '1061153932:AAFPiMBR-bpTtqAHkz_dA4sTvsS-ktgUWQ4'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_message(msg):
    name = msg.chat.first_name
    cid = msg.chat.id
    bot.send_message(chat_id=cid, text='Hello, '+name, reply_markup=create_keyboard(menu))

def create_keyboard(words=None, width=1, isOneTime=False, isPhone=False):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=isOneTime, row_width=width, resize_keyboard = True)
    for word in words:
        keyboard.add(types.KeyboardButton(text=word, request_contact=isPhone))
    return keyboard

menu = ['Adress', 'Contacts', 'Questions']
questions = ['На какие цели могу я получить кредит?', 'Что такое Интернет-банк?', 'С какого возраста можно открыть депозит?', 'Сколько стоить открыть кредит?', 'Могу ли получить арендное жильё?', 'Почему мне выгодно открыть депозит жилищных-строительных сбережений?', 'Ск']

@bot.message_handler(content_types=['text'])
def send_message(msg):
    cid = msg.chat.id
    content = msg.text
    if content == 'Adress':
        bot.send_location(chat_id=cid, latitude=43.219141, longitude=76.846924)
    elif content == 'Contacts':
        bot.send_message(chat_id=cid, text='+7 800 080-18-80')
    elif content == 'Questions':
        bot.send_message(chat_id=cid, text='Hello world')







bot.polling(none_stop=True)



#связь со строительными кампаниями,видеть квартиры тд


import telebot, requests, bs4
from telebot import types
import json
#импортировал библиотеку для парсинга, тк с тем сайтом не удобно работать
linkval = 'https://prodengi.kz/currency/konverter_valyt/'

data = requests.get(linkval)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

photo = types.InputMedia

token = '1061153932:AAFPiMBR-bpTtqAHkz_dA4sTvsS-ktgUWQ4'

bot = telebot.TeleBot(token)

valuty1 = []
valuty2 = []
valuty3 = {}

val1 = soup.findAll('div', {'class': 'quant befor'})
text1 = soup.findAll('p')
for text in val1:
    text = text.next_element.next_element
    valuty1.append(text)

val2 = soup.findAll('div', {'class': 'price_buy befor'})
text2 = soup.findAll('p')
for text in val2:
    text = text.next_element.next_element
    valuty2.append(text)

for i in range(0, len(valuty2)):
    valuty3[valuty1[i]] = valuty2[i]

@bot.message_handler(commands=['start'])
def send_message(msg):
    cid = msg.chat.id
    bot.send_message(chat_id=cid, text='Здравствуйте!', reply_markup=create_keyboard(menu))

def send_back(msg):
    cid = msg.chat.id
    bot.send_message(chat_id=cid, text='Назад', reply_markup=create_keyboard(menu))

def create_keyboard(words=None, width=1, isOneTime=False, isPhone=False):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=isOneTime, row_width=width, resize_keyboard = True)
    for word in words:
        keyboard.add(types.KeyboardButton(text=word, request_contact=isPhone))
    return keyboard

#@bot.message_handler(commands=['url'])
def intwogis1():
    keytwogis = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text='proba',url='https://go.2gis.com/20uzt')
    keytwogis.add(url1)
    return keytwogis
def intwogis2():
    keytwogis = types.InlineKeyboardMarkup()
    url2 = types.InlineKeyboardButton(text='proba',url='https://go.2gis.com/9fxva')
    keytwogis.add(url2)
    return keytwogis
def intwogis3():
    keytwogis = types.InlineKeyboardMarkup()
    url3 = types.InlineKeyboardButton(text='proba',url='https://go.2gis.com/pr0nl2')
    keytwogis.add(url3)
    return keytwogis
def intwogis4():
    keytwogis = types.InlineKeyboardMarkup()
    url4 = types.InlineKeyboardButton(text='proba',url='https://go.2gis.com/stnlt')
    keytwogis.add(url4)
    return keytwogis
def intwogis5():
    keytwogis = types.InlineKeyboardMarkup()
    url5 = types.InlineKeyboardButton(text='proba',url='https://go.2gis.com/11pte')
    keytwogis.add(url5)
    return keytwogis


def inline(): 
    keyb = types.InlineKeyboardMarkup(8)
    but1 = types.InlineKeyboardButton('1', callback_data='1s')
    but2 = types.InlineKeyboardButton('2', callback_data='2s')
    but3 = types.InlineKeyboardButton('3', callback_data='3s')
    but4 = types.InlineKeyboardButton('4', callback_data='4s')
    but5 = types.InlineKeyboardButton('5', callback_data='5s')
    but6 = types.InlineKeyboardButton('6', callback_data='6s')
    but7 = types.InlineKeyboardButton('7', callback_data='7s')
    but8 = types.InlineKeyboardButton('8', callback_data='8s')  
    keyb.add(but1)    
    keyb.add(but2)
    keyb.add(but3)
    keyb.add(but4)
    keyb.add(but5)
    keyb.add(but6)
    keyb.add(but7)
    keyb.add(but8)   
    return keyb

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "1s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Интернет-банкинг — это общее название технологий дистанционного банковского обслуживания, а также доступ к счетам и операциям (по ним), предоставляющийся в любое время и с любого устройства, имеющего доступ в Интернет. Для выполнения операций используется браузер, то есть отсутствует необходимость установки клиентской части программного обеспечения системы. Интернет-банк позволяет клиентам банка удобно, быстро и безопасно контролировать свои счета, производить прогнозные расчеты по вкладам, направлять заявки на участие в пулах в рамках программ жилищного строительства и многое другое.')
        elif call.data == "2s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='На улучшение жилищных условий: приобретение жилища, строительство дома, ремонт и модернизация жилища, рефинансирование займов, выданных в других банках, на улучшение жилищных условий, для внесения первоначального взноса по ипотеке в других банках')
        elif call.data == "3s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Открыть депозит ЖСС можно с любого возраста. До 14 лет договор заключается законным представителем, с 14 лет до 18 лет несовершеннолетним лицом с согласия законного представителя.')
        elif call.data == "4s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Комиссионный сбор за открытие вклада ЖСС не взимается')
        elif call.data == "5s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдельного направления аренды жилья по линии Банка нет. Очередники МИО и молодые семьи имеют возможность приобрести жилье в аренду в рамках Программы "Нұрлы жер". Отбор участников осуществляет МИО. Банк производит оценку платежеспособности направляемых Вкладчиков')
        elif call.data == "6s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Открыв вклад ЖСС Вы:\n - купите любое жилье на рынке в любом регионе страны;\n - участвуете в программах 'Нұрлы жер', 'Свой дом', 'Бақытты отбасы' и в других региональных программах ('Алматы жастары', 'Орда', жилищные сертификаты);\n - построите дом своей мечты;\n - сделаете ремонт о котором давно планировали;\n - приобретете земельный участок для строительства собственного дома;\n - рефинансируете свой ипотечный кредит по низкой ставке вознаграждения - по ставке 3,5-8,5% годовых;\n - получаете ежегодно премию государства в размере 20%;\n   - оформите жилищный заем по низким и фиксированным ставкам в стране - по 3,5-5% годовых;\n - получаете льготу при уплате индивидуального подоходного налога (только для заемщиков)")
        elif call.data == "7s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Для приобретения жилья на рынке необходимо накопить либо единовременно внести 50% от договорной суммы.')
        elif call.data == "8s":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вкладчик имеет возможность приобрести жилье на рынке либо в рамках государственных и отраслевых программ жилищного строительства.')
    


menu = ['Адреса и графики работ отделений', 'Контакты', 'Частые вопросы', 'Самое важное','Курс валют']
adress = ['Центральный аппарат | пр-т. Абылай хана, 91', 'пр-т. Сейфуллина, 498', 'ул. Шевченко, 155/6', 'мкр. Жетысу-2, 70Б', 'ул. Тулебаева, 15/18А','Назад']
important = ['Всё о системе ЖС', 'Жилищный заём', 'Промежуточный заём', 'Предварительный заём', 'Назад ']


def send_adress1(msg):
    cid = msg.chat.id
    content = msg.text
    if content == 'Центральный аппарат | пр-т. Абылай хана, 91':
        bot.send_message(chat_id=cid, text='Центральный аппарат "Жилстройсбербанк Казахстана"\n\nг. Алматы, пр-т. Абылай хана, 91\nГрафик работы:\nбудние дни: 09:00 - 18:00', reply_markup=intwogis1())
        bot.send_location(chat_id=cid, latitude=43.255660, longitude=76.948611)
    elif content == 'пр-т. Сейфуллина, 498':
        bot.send_message(chat_id=cid, text='Отеделение банка,\n\nРеспублика Казахсан, .Алматы, пр-т. Сейфуллина, 498\nГрафик работы:\nбудние дни: 09:00 - 18:00', reply_markup=intwogis2())
        bot.send_location(chat_id=cid, latitude=43.235546, longitude=76.981677)
    elif content == 'ул. Шевченко, 155/6':
        bot.send_message(chat_id=cid, text='Отеделение банка,\n\nРеспублика Казахсан, г.Алматы, ул. Шевченко, 155/6\nГрафик работы:\nбудние дни: 09:00 - 18:00', reply_markup=intwogis3())
        bot.send_location(chat_id=cid, latitude=43.2437411, longitude=76.8999463)
    elif content == 'мкр. Жетысу-2, 70Б':
        bot.send_message(chat_id=cid, text='Отеделение банка,\n\nРеспублика Казахсан, г.Алматы, мкр. Жетысу-2, 70Б\nГрафик работы:\nбудние дни: 09:00 - 18:00', reply_markup=intwogis4())
        bot.send_location(chat_id=cid, latitude=43.219273, longitude=76.846908)
    elif content == 'ул. Тулебаева, 15/18А':
        bot.send_message(chat_id=cid, text='Отеделение банка,\n\nРеспублика Казахсан, г.Алматы, ул. Тулебаева, 15/18А\nГрафик работы:\nбудние дни: 09:00 - 18:00', reply_markup=intwogis5())
        bot.send_location(chat_id=cid, latitude=43.26699, longitude=76.946132)
    elif content == 'Назад':
        send_back(msg)

def send_important(msg):
    cid = msg.chat.id
    content = msg.text
    if content == 'Всё о системе ЖС':#в каждой условной конструкции должны будут быть кластеры картинками от артёма
        bot.send_message(chat_id=cid, text='разработка') 
    elif content == 'Жилищный заём':
        bot.send_message(chat_id=cid, text='разработка')
    elif content == 'Промежуточный заём':
        bot.send_message(chat_id=cid, text='разработка')
    elif content == 'Предварительный заём':
        bot.send_message(chat_id=cid, text='разработка')
    elif content == 'Назад ':
        send_back(msg)



@bot.message_handler(content_types=['text'])
def send_message1(msg):
    cid = msg.chat.id
    content = msg.text
    send_adress1(msg)
    send_important(msg)
    if content == 'Адреса и графики работ отделений':
        bot.send_message(chat_id=cid, text='Адреса и графики работ отделений', reply_markup=create_keyboard(adress))
    elif content == 'Контакты':
        bot.send_message(chat_id=cid, text='+77273309300\n+77272793511\n+77273307590')
    elif content == 'Частые вопросы': 
        bot.send_message(chat_id=cid, text='Выберите интерисующий вопрос:\n'+'1.Что такое Интернет-банк?\n'+'2.На какие цели могу я получить кредит?\n'+'3.С какого возраста можно открыть депозит?\n'+'4.Сколько стоит открыть кредит?\n'+'5.Могу ли получить арендное жильё?\n'+'6.Почему мне выгодно открыть депозит жилищных-строительных сбережений?\n'+'7.Сколько я должен накопить чтобы приобрести жильё?\n'+'8.Как я могу приобрести жильё?', reply_markup=inline())
    elif content == 'Курс валют':
        bot.send_message(chat_id=cid, text='1 Доллар США'+'='+valuty3['1 Доллар США'])
        bot.send_message(chat_id=cid, text='1 Евро'+'='+valuty3['1 Евро'])
        bot.send_message(chat_id=cid, text='1 Российский рубль'+'='+valuty3['1 Российский рубль'])
    elif content == 'Самое важное':
        bot.send_message(chat_id=cid, text='Самое важное', reply_markup=create_keyboard(important))

#если отправить все валюты одним соообщением, он, почему-то выдаст ошибку, с этим ещё нужно будет разобраться, снизу код, можешь проверить
#bot.send_message(chat_id=cid, text='1 Доллар США'+'='+valuty3['1 Доллар США'], '\n1 Евро'+'='+valuty3['1 Евро'], '\n1 Российский рубль'+'='+valuty3['1 Российский рубль'])
#в словаре valuty3 сейчас есть практически все валюты, мб это нам пригодится




bot.polling(none_stop=True)


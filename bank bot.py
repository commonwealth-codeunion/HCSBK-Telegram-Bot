import telebot
from telebot import types
import requests


linkval = 'https://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40'

data = requests.get(linkval)
slovar = data.json()
valuty = slovar['rates']

CallBackButtonCredit = 'callbackbuttoncredit'
CallBackButtonIntBank = 'callbackbuttonintbank'
CallBackButtonDepozit = 'callbackbuttondepozit'
CallBackButtonKredit = 'callbackbuttonkredit'
CallBackButtonHata = 'callbackbuttonhata'
CallBackButtonStroyHata = 'callbackbuttonstroyhata'
CallBackButtonKopilka = 'callbackbuttonkopilka'
CallBackButtonKupluGarazh = 'callbackbuttonkuplugarazh'

FAQ = {
    CallBackButtonCredit:'На какие цели могу я получить кредит?',
    CallBackButtonIntBank:'Что такое Интернет-банк?',
    CallBackButtonDepozit:'С какого возраста можно открыть депозит?',
    CallBackButtonKredit:'Сколько стоит открыть кредит?',
    CallBackButtonHata:'Могу ли получить арендное жильё?',
    CallBackButtonStroyHata:'Почему мне выгодно открыть депозит жилищных-строительных сбережений?',
    CallBackButtonKopilka:'Сколько я должен накопить чтобы приобрести жильё?',
    CallBackButtonKupluGarazh:'Как я могу приобрести жильё?'}

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

#@bot.message_handler(content_types=['text'])
def inline(): 
    keyb = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton(FAQ[CallBackButtonCredit], callback_data='CallBackButtonCredit')
    but2 = types.InlineKeyboardButton(FAQ[CallBackButtonIntBank], callback_data='CallBackButtonIntBank')
    but3 = types.InlineKeyboardButton(FAQ[CallBackButtonDepozit], callback_data='CallBackButtonDepozit')
    but4 = types.InlineKeyboardButton(FAQ[CallBackButtonKredit], callback_data='CallBackButtonKredit')
    but5 = types.InlineKeyboardButton(FAQ[CallBackButtonHata], callback_data='CallBackButtonHata')
    but6 = types.InlineKeyboardButton(FAQ[CallBackButtonStroyHata], callback_data='CallBackButtonStroyHata')
    but7 = types.InlineKeyboardButton(FAQ[CallBackButtonKopilka], callback_data='CallBackButtonKopilka')
    but8 = types.InlineKeyboardButton(FAQ[CallBackButtonKupluGarazh], callback_data='CallBackButtonKupluGarazh')  
    keyb.add(but1) 
    keyb.add(but2)
    keyb.add(but3)
    keyb.add(but4)
    keyb.add(but5)
    keyb.add(but6)
    keyb.add(but7)
    keyb.add(but8) 
    return keyb
    
#бля 4 утра я тебе завтра кароч объясню что к чему, сорян
#я тип сделал менюшку эту, но ее нужно красиво сделать и ещё чтобы ответы давала


menu = ['Adress', 'Contacts', 'Questions']
questions = ['На какие цели могу я получить кредит?', 'Что такое Интернет-банк?', 'С какого возраста можно открыть депозит?', 'Сколько стоит открыть кредит?', 'Могу ли получить арендное жильё?', 'Почему мне выгодно открыть депозит жилищных-строительных сбережений?', 'Сколько я должен накопить чтобы приобрести жильё?', 'Как я могу приобрести жильё?']

@bot.message_handler(content_types=['text'])
def send_message1(msg):
    cid = msg.chat.id
    content = msg.text
    if content == 'Adress':
        bot.send_location(chat_id=cid, latitude=43.219141, longitude=76.846924)
    elif content == 'Contacts':
        bot.send_message(chat_id=cid, text='+7 800 080-18-80')
    elif content == 'Questions': 
        bot.send_message(chat_id=cid, text='Выберите интерисующий вопрос: ', reply_markup=inline())      



        '''
        bot.send_message(chat_id=cid, text='Часто задаваемые вопросы', reply_markup=create_keyboard(questions))
        if content == 'На какие цели могу я получить кредит?':
            bot.send_message(chat_id=cid, text='На улучшение жилищных условий: приобретение жилища, строительство дома, ремонт и модернизация жилища, рефинансирование займов, выданных в других банках, на улучшение жилищных условий, для внесения первоначального взноса по ипотеке в других банках')
        elif content == 'Что такое Интернет-банк?':
            bot.send_message(chat_id=cid, text='Интернет-банкинг - это общее название технологий дистанционного банковского обслуживания, а также доступ к счетам и операциям (по ним), предоставляющийся в любое время и с любого устройства, имеющего доступ в Интернет. Для выполнения операций используется браузер, то есть отсутствует необходимость установки клиентской части программного обеспечения системы. Интернет-банк позволяет клиентам банка удобно, быстро и безопасно контролировать свои счета, производить прогнозные расчеты по вкладам, направлять заявки на участие в пулах в рамках программ жилищного строительства и многое другое.')
        elif content == 'С какого возраста можно открыть депозит?':
            bot.send_message(chat_id=cid, text='Открыть депозит ЖСС можно с любого возраста. До 14 лет договор заключается законным представителем, с 14 лет до 18 лет несовершеннолетним лицом с согласия законного представителя.')
        elif content == 'Сколько стоит открыть кредит?':
            bot.send_message(chat_id=cid, text='Комиссионный сбор за открытие вклада ЖСС не взимается')
        elif content == 'Могу ли получить арендное жильё?':
            bot.send_message(chat_id=cid, text='Отдельного направления аренды жилья по линии Банка нет. Очередники МИО и молодые семьи имеют возможность приобрести жилье в аренду в рамках Программы "Нұрлы жер". Отбор участников осуществляет МИО. Банк производит оценку платежеспособности направляемых Вкладчиков')
        elif content == 'Почему мне выгодно открыть депозит жилищных-строительных сбережений?':
            bot.send_message == "Открыв вклад ЖСС Вы:\n - купите любое жилье на рынке в любом регионе страны;\n - участвуете в программах 'Нұрлы жер', 'Свой дом', 'Бақытты отбасы' и в других региональных программах ('Алматы жастары', 'Орда', жилищные сертификаты);\n - построите дом своей мечты;\n - сделаете ремонт о котором давно планировали;\n - приобретете земельный участок для строительства собственного дома;\n - рефинансируете свой ипотечный кредит по низкой ставке вознаграждения - по ставке 3,5-8,5% годовых;\n - получаете ежегодно премию государства в размере 20%;\n   - оформите жилищный заем по низким и фиксированным ставкам в стране - по 3,5-5% годовых;\n - получаете льготу при уплате индивидуального подоходного налога (только для заемщиков)"  
        '''


bot.polling(none_stop=True)



#связь со строительными кампаниями,видеть квартиры тд

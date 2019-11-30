import bs4
import requests
import telebot
from telebot import types
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

menu = ['Адреса и графики работ отделений', 'Контакты', 'Частые вопросы', 'Самое важное', 'Накопить', 'Конвертация', 'Личный кабинет']
adress = ['Центральный аппарат | пр-т. Абылай хана, 91', 'пр-т. Сейфуллина, 498', 'ул. Шевченко, 155/6', 'мкр. Жетысу-2, 70Б', 'ул. Тулебаева, 15/18А','Назад']
important = ['Всё о системе ЖС', 'Жилищный займ', 'Промежуточный займ', 'Предварительный займ', 'Назад ']
convert = ['🇰🇿', '🇷🇺', '🇺🇸', '🇪🇺', 'Назад  ']
cabinet = ['Информация', 'Настройки', 'Назад   ']
nakop = ['Всё о депозите "БАСПАНА"', 'Премия государства', 'Семейный пакет', 'Подарочный сертификат', 'Детский депозит', 'Клуб лояльных клиентов', 'Назад    ']

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



@bot.message_handler(commands=['start']) #helloMessage
def send_message(msg):
    cid = msg.chat.id
    bot.send_message(chat_id=cid, text='Здравствуйте! Это телеграм-бот Жилстройсбербанка.', reply_markup=create_keyboard(menu))

def send_back(msg): #backFunction
    cid = msg.chat.id
    bot.send_message(chat_id=cid, text='Главное меню', reply_markup=create_keyboard(menu))

def create_keyboard(words=None, width=1, isOneTime=False, isPhone=False):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=isOneTime, row_width=width, resize_keyboard = True)
    for word in words:
        keyboard.add(types.KeyboardButton(text=word, request_contact=isPhone))
    return keyboard

#mainMenu
@bot.message_handler(content_types=['text'])
def send_message1(msg):
    cid = msg.chat.id
    content = msg.text
    send_adress1(msg)
    send_important(msg)
    send_convert(msg)
    send_cab(msg)
    send_nakop(msg)
    if content == menu[0]:
        bot.send_message(chat_id=cid, text='Адреса и графики работ отделений', reply_markup=create_keyboard(adress))
    elif content == menu[1]:
        bot.send_message(chat_id=cid, text='+77273309300\n\n+77272793511\n\n+77273307590')
    elif content == menu[2]: 
        bot.send_message(chat_id=cid, text='Выберите интересующий вопрос:\n'+'1.Что такое Интернет-банк?\n'+'2.На какие цели могу я получить кредит?\n'+'3.С какого возраста можно открыть депозит?\n'+'4.Сколько стоит открыть кредит?\n'+'5.Могу ли получить арендное жильё?\n'+'6.Почему мне выгодно открыть депозит жилищных-строительных сбережений?\n'+'7.Сколько я должен накопить чтобы приобрести жильё?\n'+'8.Как я могу приобрести жильё?', reply_markup=inline())
    elif content == menu[3]:
        bot.send_message(chat_id=cid, text='Самое важное', reply_markup=create_keyboard(important))
    elif content == menu[4]:
        bot.send_message(chat_id=cid, text='Накопить', reply_markup=create_keyboard(nakop))
    elif content == menu[5]:
        bot.send_message(chat_id=cid, text='Курс валют\n1 Доллар США'+' = '+valuty3['1 Доллар США']+'\n1 Евро'+' = '+valuty3['1 Евро']+'\n1 Российский рубль'+' ='+valuty3['1 Российский рубль'] + '\n\nВыберите валюту', reply_markup=create_keyboard(convert))
    elif content == menu[6]:
        bot.send_message(chat_id=cid, text='Личный кабинет', reply_markup=create_keyboard(cabinet))
#mainMenu

#adress
def send_adress1(msg):
    cid = msg.chat.id
    content = msg.text
    if content == adress[0]:
        bot.send_message(chat_id=cid, text='Центральный аппарат "Жилстройсбербанк Казахстана"\n\nг. Алматы, пр-т. Абылай хана, 91\nГрафик работы: будние дни: 09:00 - 18:00', reply_markup=intwogis1())
        bot.send_location(chat_id=cid, latitude=43.255660, longitude=76.948611)
    elif content == adress[1]:
        bot.send_message(chat_id=cid, text='Отеделение банка\n\nРеспублика Казахсан, .Алматы, пр-т. Сейфуллина, 498\nГрафик работы: будние дни: 09:00 - 18:00', reply_markup=intwogis2())
        bot.send_location(chat_id=cid, latitude=43.235546, longitude=76.981677)
    elif content == adress[2]:
        bot.send_message(chat_id=cid, text='Отеделение банка\n\nРеспублика Казахсан, г.Алматы, ул. Шевченко, 155/6\nГрафик работы: будние дни: 09:00 - 18:00', reply_markup=intwogis3())
        bot.send_location(chat_id=cid, latitude=43.2437411, longitude=76.8999463)
    elif content == adress[3]:
        bot.send_message(chat_id=cid, text='Отеделение банка\n\nРеспублика Казахсан, г.Алматы, мкр. Жетысу-2, 70Б\nГрафик работы: будние дни: 09:00 - 18:00', reply_markup=intwogis4())
        bot.send_location(chat_id=cid, latitude=43.219273, longitude=76.846908)
    elif content == adress[4]:
        bot.send_message(chat_id=cid, text='Отеделение банка\n\nРеспублика Казахсан, г.Алматы, ул. Тулебаева, 15/18А\nГрафик работы: будние дни: 09:00 - 18:00', reply_markup=intwogis5())
        bot.send_location(chat_id=cid, latitude=43.26699, longitude=76.946132)
    elif content == adress[5]:
        send_back(msg)

def intwogis1():
    keytwogis = types.InlineKeyboardMarkup()
    url1 = types.InlineKeyboardButton(text='2GIS',url='https://go.2gis.com/20uzt')
    keytwogis.add(url1)
    return keytwogis
def intwogis2():
    keytwogis = types.InlineKeyboardMarkup()
    url2 = types.InlineKeyboardButton(text='2GIS',url='https://go.2gis.com/9fxva')
    keytwogis.add(url2)
    return keytwogis
def intwogis3():
    keytwogis = types.InlineKeyboardMarkup()
    url3 = types.InlineKeyboardButton(text='2GIS',url='https://go.2gis.com/pr0nl2')
    keytwogis.add(url3)
    return keytwogis
def intwogis4():
    keytwogis = types.InlineKeyboardMarkup()
    url4 = types.InlineKeyboardButton(text='2GIS',url='https://go.2gis.com/stnlt')
    keytwogis.add(url4)
    return keytwogis
def intwogis5():
    keytwogis = types.InlineKeyboardMarkup()
    url5 = types.InlineKeyboardButton(text='2GIS',url='https://go.2gis.com/11pte')
    keytwogis.add(url5)
    return keytwogis
#adress

#menuInline_Questions
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
    keyb.row(but1, but2, but3, but4)    
    keyb.row(but5, but6, but7, but8)
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
#menuInline_Questions

#importat
def send_important(msg):
    cid = msg.chat.id
    content = msg.text
    if content == important[0]:
        bot.send_message(chat_id=cid, text='ВСЕ О СИСТЕМЕ ЖИЛСТРОЙСБЕРЕЖЕНИЙ\nУНИКАЛЬНЫЙ СПОСОБ ПОЛУЧИТЬ ИПОТЕЧНЫЙ КРЕДИТ ПО СТАВКЕ 5% И НИЖЕ!\n\nКАК ЭТО РАБОТАЕТ?\n1.Откройте депозит в Жилстройсбербанке\n2.Выполните всего три условия:\nкопите на депозите средства не менее трех лет\nнакопите половину необходимой вам суммы (50%)\nдостигните минимального уровня оценочного показателя (ОП)\n\nЕсли вы выполнили все три условия – вы получаете кредит, который называется жилищный займ, по ставке 5% годовых\n\nЕсли вы ПЕРЕвыполнили эти условия, то есть копили дольше – ставка по займу снижается (минимальная ставка 3,5%)\n\nНа сумму ваших накоплений ежегодно начисляется вознаграждение Банка и премия государства.\nЖилье на полученный кредит можно купить в любом городе страны., ВАМ ТАКЖЕ НЕОБХОДИМО ЗНАТЬ НЕСКОЛЬКО ВАЖНЫХ ТЕРМИНОВ СИСТЕМЫ ЖИЛСТРОЙСБЕРЕЖЕНИЙ:\nдоговорная сумма\nпремия государства\nоценочный показатель', reply_markup=prem())
    elif content == important[1]:
        bot.send_message(chat_id=cid, text='ВСЁ О ЖИЛИЩНОМ ЗАЁМЕ\nСтавка: от 3,5 до 5% годовых (годовая эффективная ставка от 4%)\nСумма: до 100 000 000 тенге\nЗалог: приобретаемое\n\nДЛЯ ТОГО ЧТОБЫ ПОЛУЧИТЬ САМЫЙ ВЫГОДНЫЙ КРЕДИТ, ВАМ НЕОБХОДИМО:\n1. Открыть депозит в Жилстройсбербанке\n\n2. Выполнить всего три условия:\n    ☑ копить на депозите средства не менее трех лет\n    ☑ накопить половину необходимой вам суммы (50%)\n    ☑ достичь минимального уровня оценочного показателя ОП-16\n\nЕсли вы ПЕРЕвыполнили эти условия, то есть копили дольше - ставка по займу снижается\n\nДругие преимущеста\n0% комиссии за рассмотрение кредитной заявки и организацию выдачи займа\nУпрощенная процедура подтверждения платежеспособности', reply_markup=prem())
    elif content == important[2]:
        bot.send_message(chat_id=cid, text='Если срок ваших накоплений менее трех лет, но у вас уже есть 50% от стоимости жилья, то вы можете получить промежуточный займ.\n\nНачальная ставка: от 7 до 8,5% годовых с последующим снижением до 5% ГЭСВ - от 7,4%\nСумма: до 90 000 00 тенге\nСрок кредитования: до 6 лет\n\nНАЧАЛЬНАЯ СТАВКА ПО ПРОМЕЖУТОЧНОМУ ЗАЙМУ ДЕЙСТВУЕТ ДО ТОГО МОМЕНТА, ПОКА ВАШЕМУ ДЕПОЗИТУ НЕ ИСПОЛНИТСЯ 3 ГОДА. ЗАТЕМ ВЫ ПЕРЕХОДИТЕ НА УСЛОВИЯ ЖИЛИЩНОГО ЗАЙМА, И СТАВКА ПО КРЕДИТУ СНИЖАЕТСЯ ДО 5%.\n\nВАЖНО! 50% от стоимости жилья, которые вы внесли на депозит, являются залогом. На него, как и на любой другой депозит, начисляются вознаграждение банка и ежегодная премия государства. В итоге ваш залог приносит вам доход.\n\n4 ШАГА К ПОЛУЧЕНИЮ ПРОМЕЖУТОЧНОГО ЗАЙМА:\n1. Открыть депозит в Жилстройбанке\n2. Внести на депозит 50% стоимости жилья (частями или единовременно)\n3. Подтвердить платежеспособность\n4. Получить займ', reply_markup=prem())
    elif content == important[3]:
        bot.send_message(chat_id=cid, text='ПРЕДВАРИТЕЛЬНЫЕ ЗАЙМЫ ЖИЛСТРОЙСБЕРБАНК ВЫДАЁТ ТОЛЬКО В РАМКАХ ГОСУДАРСТВЕННЫХ ПРОГРАММ И СОБСТВЕННОЙ ПРОГРАММЫ «СВОЙ ДОМ»\n\nПредварительный заём - это льготный заём, который можно получить заранее, имея на депозите всего 20% от суммы, необходимой на покупку жилья, при этом ставка по кредиту будет такая же, как у жилищного займа - 5% годовых.\n\nПри получении предварительного займа сумма вашей ежемесячной оплаты по кредиту\n  💰 одна часть суммы идет в счет погашения процентов по кредиту\n  💰 другая часть суммы пополняет ваш депозит до необходимых 50%\n\nПри этом на депозит начисляются вознаграждение банка 2% годовых и премия государства 20% от суммы накоплений.\nТолько после того, как на вашем депозите накопится 50% от договорной суммы, вы начинаете погашать основной долг и продолжаете погашать проценты по нему.\n\n6 ШАГОВ К ПОЛУЧЕНИЮ ПРЕДВАРИТЕЛЬНОГО ЗАЙМА:\n  1. Открыть депозит в Жилстройсбербанке\n  2.Выбрать жилой объект на портале baspana.kz – жилой комплекс или дом, которые строят по программе\n  3. Подать заявку на участие в пуле (это список желающих купить жилье в данном объекте) на портале baspana.kz\n  4. Накопить или положить на депозит не менее 20% от стоимости жилья\n  5. Подтвердить платежеспособность\n  6. Получить предварительный займ', reply_markup=prem())
    elif content == important[4]:
        send_back(msg)

#urlInline1
def prem():
    keyprem = types.InlineKeyboardMarkup()
    prem1 = types.InlineKeyboardButton(text='Узнать больше о премии государства', url='https://hcsbk.kz/ru/save/state-award/')
    opend = types.InlineKeyboardButton(text='Открыть депозит', url='https://hcsbk.kz/ru/save/helpful-information/how-to-open/')
    dog = types.InlineKeyboardButton(text='Узнать больше о договороной сумме', url='https://hcsbk.kz/ru/most-important/helpful-information/contractual-amount/')
    ocenka = types.InlineKeyboardButton(text='Узнать больше об оценочном показателе', url='https://hcsbk.kz/ru/most-important/helpful-information/performance-indicator/')
    keyprem.add(ocenka)
    keyprem.add(dog)
    keyprem.add(prem1)
    keyprem.add(opend) 
    return keyprem
#urlInline1
#important

#nakop
def send_nakop(msg):
    cid = msg.chat.id
    content = msg.text
    if content == nakop[0]:
        bot.send_message(chat_id=cid, text='ВСЁ О ДЕПОЗИТЕ «БАСПАНА»\n\nЭто вклад Жилищно-Строительных Сбережений, открыв который, вы получаете возможность приобрести жилье по одной из программ жилищного кредитования Жилстройсбербанка.\n\nУСЛОВИЯ ДЕПОЗИТА “БАСПАНА”\n  • Ставка вознаграждения: 2% годовых\n  • Эффективная ставка вознаграждения: до 13% годовых (с учетом премии государства)\n  • Ежегодная премия государства: 20%* (на сумму накоплений за год до 200 МРП)\n  • Минимальный срок накопления: от 3 лет\n  • Комиссия за открытие депозита: 0 тенге\n\nС КАКОГО ВОЗРАСТА МОЖНО ОТКРЫТЬ ДЕПОЗИТ?\n  👶🏻 C 0 до 14 лет | Родители или опекуны могут открыть на ребенка\n  👦🏻👧🏻 С 14 до 18 лет | При согласии родителей или опекунов\n  👨🏻👩🏻 C 18 лет | При наличии удостоверения\n\nНА КОГО Я МОГУ ОТКРЫТЬ ДЕПОЗИТ?\n  👨🏻 На себя\n  👪 На своего ребёнка\n  📋 На третье лицо при наличии доверенности на открытие счета\n\n КАК ОТКРЫТЬ ДЕПОЗИТ?\nМы предлагаем вам четыре способа:\n  ☑ В любом удобном для вас месте – через консультантов Жилстройсбербанка\n  ☑ В Консультационном центре вашего города\n  ☑ В любом отделении Жилстройсбербанка\n  В отделении АО «Казпочта»\nПри открытии депозита и заключении договора о жилстройсбережениях вам нужно указать договорную сумму и срок накопления. Исходя из этих двух показателей рассчитывается ежемесячный взнос на депозит.\nЕЖЕМЕСЯЧНЫЙ ВЗНОС\nРассчитывается с учетом договорной суммы и коэффициента взноса:\n Ежемесячный взнос = Договорная сумма х Коэффициент взноса\nКоэффициент взноса по депозиту зависит от срока накопления: чем больше срок - тем ниже коэффициент взноса. К примеру, на срок накопления 3 года коэффицент взноса будет равен 1.5%\n\nСПОСОБЫ ПОПОЛНЕНИЯ ДЕПОЗИТА\n  Через терминалы Жилстройсбербанка\n  В отделении Жилстройсбербанка\n  Через интернет-банкинг ЖССБ\n  Через интернет-банкинг и отделения других банков\n  В отделениях Казпочты', reply_markup=send_inNakop())
    elif content == nakop[1]:
        bot.send_message(chat_id=cid, text='ПРЕМИЯ ГОСУДАРСТВА\n\nПРЕМИЯ ГОСУДАРСТВА - ЭТО СРЕДСТВА ИЗ РЕСПУБЛИКАНСКОГО БЮДЖЕТА, КОТОРЫЕ НАЧИСЛЯЮТСЯ НА ДЕПОЗИТЫ ВКЛАДЧИКОВ ЖИЛСТРОЙСБЕРБАНКА ДЛЯ ПОДДЕРЖКИ ИХ СТРЕМЛЕНИЙ УЛУЧШИТЬ ЖИЛИЩНЫЕ УСЛОВИЯ\nПремия государства зачисляется ежегодно по итогам календарного года. Деньги зачисляются единовременно на все депозиты в первом квартале каждого года. Если до конца года вы накопили 200 МРП, то Вам будет начислена максимальная сумма премии\n\n⚠️ЧТО НУЖНО ЗАПОМНИТЬ?⚠️\n  Размер премии государства - 20% от суммы накоплений за год, не превышающей 200 МПР. Премия государства начисляется на те деньги, которые вы положили на депозит в течение года, но не более, чем на 200 МРП.\n  Если ваши накопления за год составили больше 200 МРП, то на сумму, превышающую лимит, Премия Государства будет начислена в следующем году.\n  Один вкладчик может иметь несколько счетов жилстройсбережений, но Премия Государства начисляется только на один из его счетов.\n  Премия государства начисляется также на депозиты, являющиеся залогом при получении промежуточных и предварительных займов.\n  Премия Государства начисляется только на счет вкладчика, являющегося гражданином РК.\n  Премия Государства не начисляется на поощренную ранее сумму вклада.\n  Если вы накапливали сбережения менее трех лет и решили досрочно закрыть депозит, Премия Государства возвращается в бюджет.\n  Если вы получили жилищный займ, но использовали его не для улучшения жилищных условий, Премия Государства возвращается в бюджет.\n\nПОПОЛНИТЕ СВОЙ ВКЛАД В ЖИЛСТРОЙСБЕРБАНКЕ СЕГОДНЯ И ПОЛУЧИТЕ ПРЕМИЮ В НАЧАЛЕ ГОДА!', reply_markup=send_premGos())
    elif content == nakop[2]:
        bot.send_message(chat_id=cid, text='СЕМЕЙНЫЙ ПАКЕТ\n\nХотите увеличить свои накопления? Все что для этого нужно - открыть депозиты на нескольких членов семьи.\nТогда премия государства будет начисляться на каждый из этих депозитов. Перед получением займа вы можете объединить депозиты «Семейного пакета» в один вклад и получить общий жилищный заем, сохранив премии всех членов семьи.\n\n⚠️ «Семейный пакет» можно использовать для всех близких родственников: супруги, родители, дети, братья и сестры. Откройте депозиты в рамках «семейного пакета» на себя и членов своей семьи и увеличьте свой доход по депозиту!\n\nСРАВНИТЕ НА ПРИМЕРЕ\n👨🏻 Персональный вклад\n  Один вкладчик может иметь несколько депозитов, но премия государства начисляется только на один из счетов.\n  Ежемесячные взносы 83 000 тг\n  Премия государства за весь период 481 000 тг\n  % банка за весь период 261 652 тг\n  Общие накопления 5 722 652 тг\n👨🏻👩🏻 Семейный пакет\n  Если открыть депозиты на всех членов своей семьи, то премия будет начисляться на каждый депозит «Семейного пакета».\n    Ежемесячные взносы 83 000 тг\n  Премия государства за весь период 481 000 тг\n  % банка за весь период 261 652 тг\n  Общие накопления 6 203 652 тг\nСроки накопления 5 лет', reply_markup=send_premGos())
    elif content == nakop[3]:
        bot.send_message(chat_id=cid, text='ПОДАРОЧНЫЙ СЕРТИФИКАТ\n\nДействительно полезный подарок на свадьбу, день рождения, семейное торжество от друзей, родственников или коллег - сертификат на открытие депозита в Жилстройсбербанке с начальной суммой взноса. Стоимость сертификата равна сумме первого взноса на депозит того человека, которому вы подарите сертификат.\n\nОСНОВНЫЕ ПАРАМЕТРЫ ПОДАРОЧНОГО СЕРТИФИКАТА\n  Минимальная сумма - 5 000 тг\n  Подарочный сертификат действителен 3 месяца\n  Максимальная сумма - не ограничена\n  Каждый сертификат имеет свой код для идентификации\n\nДля тех, кто хочет подарить:\n  1. Прийти в ближайшее отделение банка. При себе необходимо иметь свое удостоверение личности.\n  2. Заполнить заявление на заключение договора о жилищных строительных сбережениях (договор открывается без указания имени и фамилии лица, которому будет подарен сертификат).\nКАК ПРИОБРЕСТИ ПОДАРОЧНЫЙ СЕРТИФИКАТ?\n  3. Заполнить заявление на получение сертификата.\n  4. Оплатить в кассе сумму сертификата.\n  5. Получить сертификат для подарка.\n\nДля тех, кто получил в подарок:\n  1. Прийти в ближайшее отделение банка с оригиналом сертификата. При себе необходимо иметь свое удостоверение личности.\n  2. Переоформить договор о жилищных строительных сбережениях на свое имя (договор в банке был открыт при покупке подарочного сертификата).\nКАК АКТИВИРОВАТЬ ПОДАРОЧНЫЙ СЕРТИФИКАТ?\n  3. При активации договора можно будет увеличить договорную сумму и изменить срок накопления.\n  4. Подписать заявление на присоединение к Стандартным условиям комплексного банковского обслуживания в АО "Жилстройсбербанк Казахстана".\nЕсли по истечении 3-х месяцев сертификат не был активирован, то он автоматически остается в виде депозита на того человека, который купил данный сертификат для подарка.', reply_markup=send_premGos())
    elif content == nakop[4]:
        bot.send_message(chat_id=cid, text='ДЕТСКИЙ ДЕПОЗИТ\nВ ЖИЛСТРОЙСБЕРБАНКЕ ВЫ МОЖЕТЕ ОТКРЫТЬ ПЕРСОНАЛЬНЫЙ ДЕПОЗИТ НА СВОЕГО РЕБЕНКА С ПЕРВЫХ ДНЕЙ ЕГО ЖИЗНИ!\n\nДетский депозит имеет все преимущества депозитов Жилстройсбербанка:\n  • на него начисляется вознаграждение банка 2% и премия государства в размере 20% от суммы накоплений за год (максимально на 200 МРП);\n  • он может стать частью Семейного пакета и таким образом увеличить доход по накоплениям всей семьи;\n  • при достижении 3-летнего срока накопления, половины договорной суммы и необходимого уровня Оценочного показателя он дает право на получение кредита по ставке 5% и ниже (если владельцу депозита исполнилось 18 лет).\n\nКАК ОТКРЫТЬ ДЕТСКИЙ ДЕПОЗИТ?\nЕсли ребенку не исполнилось 14 лет:\n  До 14 лет депозиты на детей могут открыть только взрослые: родители или другие законные представители (например, опекуны).\n  При открытии депозита на ребенка до 14-ти лет требуется его свидетельство о рождении. Один из родителей/законных представителей также должен иметь при себе свое удостоверение личности.\nЕсли ребенку исполнилось 14 лет:\n  С 14 лет ребенок может самостоятельно открыть депозит в Жилстройсбербанке, но с согласия родителей.\n  При открытии с 14 лет также требуется его свидетельство о рождении, договор открывается несовершеннолетним лицом с письменного согласия законного представителя.', reply_markup=send_premGos())
    elif content == nakop[5]:
        bot.send_message(chat_id=cid, text='Разработка')
    elif content == nakop[6]:
        send_back(msg)
#inline
def send_inNakop():
    keyinNakop = types.InlineKeyboardMarkup()
    childDep_inNakop = types.InlineKeyboardButton(text='Подробнее о детских депозитах', url='https://hcsbk.kz/ru/save/childrens-deposit/')
    consult_inNakop = types.InlineKeyboardButton(text='Получить консультацию', url='https://hcsbk.kz/ru/network-agents/')
    depos_inNakop=types.InlineKeyboardButton(text='Как открыть депозит?', url='https://hcsbk.kz/ru/save/helpful-information/how-to-open/')
    secDepos_inNakop=types.InlineKeyboardButton(text='Второй депозит', url='https://hcsbk.kz/ru/save/helpful-information/second-deposit/')
    ustup_inNakop=types.InlineKeyboardButton(text='Все об уступке депозита несовершеннолетних', url='https://hcsbk.kz/ru/save/helpful-information/order-concessions-from-minors/')
    keyinNakop.add(childDep_inNakop)
    keyinNakop.add(consult_inNakop)
    keyinNakop.add(depos_inNakop)
    keyinNakop.add(secDepos_inNakop)
    keyinNakop.add(ustup_inNakop)
    return keyinNakop
def send_premGos():
    keypremGos = types.InlineKeyboardMarkup()
    depos_premGos=types.InlineKeyboardButton(text='Как открыть депозит?', url='https://hcsbk.kz/ru/save/helpful-information/how-to-open/')
    secDepos_premGos=types.InlineKeyboardButton(text='Второй депозит', url='https://hcsbk.kz/ru/save/helpful-information/second-deposit/')
    ustup_premGos=types.InlineKeyboardButton(text='Все об уступке депозита несовершеннолетних', url='https://hcsbk.kz/ru/save/helpful-information/order-concessions-from-minors/')
    consult_premGos = types.InlineKeyboardButton(text='Получить консультацию', url='https://hcsbk.kz/ru/network-agents/')
    keypremGos.add(depos_premGos)
    keypremGos.add(secDepos_premGos)
    keypremGos.add(ustup_premGos)
    keypremGos.add(consult_premGos)
    return keypremGos
#inline
#nakop

#convertation
def send_convert(msg):
    cid = msg.chat.id
    content = msg.text
    #kztconvert = 0
    if content == convert[2]:
        sent2 = bot.send_message(chat_id=cid, text='Введите сумму')
        bot.register_next_step_handler(sent2, convUs)
        #eurconvert = content
    elif content == convert[0]:
        sent = bot.send_message(chat_id=cid, text='Введите сумму')
        #sent = bot.send_message(chat_id=cid, text=content+'тенге= '+usdconvert+'долларов Сша\n'+content+'тенге= '+eurconvert+'евро')
        bot.register_next_step_handler(sent, convKz)
    elif content == convert[3]:
        sent3 = bot.send_message(chat_id=cid, text='Введите сумму')
        bot.register_next_step_handler(sent3, convEu)
    elif content == convert[1]:
        sent4 = bot.send_message(chat_id=cid, text='Введите сумму')
        bot.register_next_step_handler(sent4, convRu)
    elif content == convert[4]:
        send_back(msg)

def convKz(msg):
    cid = msg.chat.id
    content = msg.text
    usdconvert = int(content)/float(valuty3['1 Доллар США'])
    eurconvert = int(content)/float(valuty3['1 Евро'])
    ruconvert =  int(content)/float(valuty3['1 Российский рубль'])
    bot.send_message(chat_id=cid, text=content+' тенге = '+str(round(usdconvert, 2))+' долларов США\n'+content+' тенге = '+str(round(eurconvert, 2))+' евро\n'+content+' тенге = '+str(round(ruconvert, 2)))
def convUs(msg):
    cid = msg.chat.id
    content = msg.text
    chast = float(valuty3['1 Доллар США'])/float(valuty3['1 Евро'])
    chast1 = float(valuty3['1 Доллар США'])/float(valuty3['1 Российский рубль'])
    kztconvert = int(content)*float(valuty3['1 Доллар США'])
    eurconvert = int(content)*float(chast)
    ruconvert = int(content)*float(chast1)
    bot.send_message(chat_id=cid, text=content+' долларов США = '+str(round(kztconvert, 2))+' тенге\n'+content+' долларов США = '+str(round(eurconvert, 2))+' евро\n'+content+' долларов США = '+str(round(ruconvert, 2)))
def convEu(msg):
    cid = msg.chat.id
    content = msg.text
    chast = float(valuty3['1 Евро'])/float(valuty3['1 Доллар США'])
    chast1 = float(valuty3['1 Евро'])/float(valuty3['1 Российский рубль'])
    kztconvert = int(content)*float(valuty3['1 Евро'])
    usdconvert = int(content)*float(chast)
    ruconvert = int(content)*float(chast1)
    bot.send_message(chat_id=cid, text=content+' евро = '+str(round(kztconvert, 2))+' тенге\n'+content+' евро = '+str(round(usdconvert, 2))+' долларов США\n'+content+' евро = '+str(round(ruconvert, 2)))
def convRu(msg):
    cid = msg.chat.id
    content = msg.text
    chast = float(valuty3['1 Российский рубль'])/float(valuty3['1 Доллар США'])
    chast1 = float(valuty3['1 Российский рубль'])/float(valuty3['1 Евро'])
    kztconvert = int(content)*float(valuty3['1 Российский рубль'])
    usdconvert = int(content)*float(chast)
    eurconvert = int(content)*float(chast1)
    bot.send_message(chat_id=cid, text=content+' рублей = '+str(round(kztconvert, 2))+' тенге\n'+content+' рублей = '+str(round(usdconvert, 2))+' долларов США\n'+content+' рублей = '+str(round(eurconvert, 2)))
#convertation

#cabinet
def send_cab(msg):
    cid = msg.chat.id
    content = msg.text
    if content == cabinet[0]:
        bot.send_message(chat_id=cid, text='Информация о профиле\n\nОгай Владислав Сергеевич\n\nСостояние займа №1\nСумма займа: 24 942 887 ₸\nСумма накоплений: 25 187 881 ₸\nСрок жилищного займа, мес.: 84\nСтавка в год: 4.8%\nПогашения по кредиту: 354 618.81 ₸/мес')
    elif content == cabinet[1]:
        bot.send_message(chat_id=cid, text='Настройки')
    elif content == cabinet[2]:
        send_back(msg)
#cabinet

#в словаре valuty3 сейчас есть практически все валюты, мб это нам пригодится


bot.polling(none_stop=True)
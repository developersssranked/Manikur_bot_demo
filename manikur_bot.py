import telebot



bot=telebot.TeleBot(token='5748799570:AAFGwZjuqRw5fEbq6Ep1acIkusQ3tIdWdbY')


bot.message_handler(commands=['start'])
def start(message):
    markup=telebot.types.ReplyKeyboardMarkup()
    markup.add(telebot.types.KeyboardButton('Продолжить'))
    bot.send_message(message.chat.id,'Это тестовая версия телеграм бота для записи на маникюр. Для продолжения используйте клавиатуру.',reply_markup=markup)

    
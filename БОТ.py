import telebot
bot = telebot.TeleBot('6719205536:AAERrWNZMhCoCIwJAaFrhQV4SdQ3CdM1MKw')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Салам всякому вошедшему!')

@bot.message_handler(commands=['Понедельник'])
def main(message):
    bot.send_message(message.chat.id,'Начало в 9:30, Конец в 16:00')

@bot.message_handler(commands=['Вторник'])
def main(message):
    bot.send_message(message.chat.id,'Начало в 9:30, Конец в 16:00')

@bot.message_handler(commands=['Среда'])
def main(message):
    bot.send_message(message.chat.id,'Начало в 13:00, Конец в 17:40')

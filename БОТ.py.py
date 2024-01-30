import telebot
import csv

bot = telebot.TeleBot('6719205536:AAERrWNZMhCoCIwJAaFrhQV4SdQ3CdM1MKw')

with open("Расписание.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    for row in file_reader:
        command = row[0]
        message_text = f"{row[1]}\n{row[2]}"

        @bot.message_handler(commands=[command])
        def handle_message(message):
            bot.send_message(message.chat.id, message_text)

# Запуск бота
bot.polling(none_stop=True)





import telebot
import csv
from dotenv import load_dotenv
import os
load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
schedule = {}
with open("Расписание.csv", encoding='utf-8-sig') as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    for row in file_reader:
        command = row[0]
        message_text = f"{row[2]}\n{row[1]}"
        if schedule.get(command, None):
            schedule[command] = schedule[command] + "\n" + message_text
        else:
            schedule[command] = message_text

@bot.message_handler(commands=["Вторник"])
def handle_message(message):
    bot.send_message(message.chat.id, schedule["Вторник"])
@bot.message_handler(commands=["Понедельник"])
def handle_message(message):
    bot.send_message(message.chat.id, schedule["Понедельник"])
# Запуск бота
bot.polling(none_stop=True)
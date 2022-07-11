import telebot
import os
from dotenv import load_dotenv
import requests

ANALYZER_URL = "http://127.0.0.1:8000/analyze/"
TELEBOT_AUTH_TOKEN = "TOKEN"
load_dotenv()
token = os.getenv("TELEBOT_AUTH_TOKEN")

bot = telebot.TeleBot(TELEBOT_AUTH_TOKEN)
bot.parse_mode = 'HTML'


# create main function for bot to run polling
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Тевирп! Привет, я твой бот! Я могу анализировать текст и угадывать эмоции. Напиши мне текст и я угадаю их.")


@bot.message_handler(func=lambda message: True)
def return_emotion(message):
    bot.reply_to(message, "Шуры муры, текст изучаю, эмоции получаю, туры пуры...")
    server_answer = requests.get(ANALYZER_URL + message.text)
    if server_answer.status_code == 200:
        bot.reply_to(message, f"Итак, доминирующая эмоция, которую я узнаю, это - {server_answer.json()['dominant_emotion']}")
        bot.reply_to(message, f"""А вот если разложить карты таро и погадать на составные части, то мне кажется, что тут
        🤡 - {server_answer.json()['emotions']['happiness']*100:.2f}% счастья/удовлетворения (happiness),
        🤡 - {server_answer.json()['emotions']['anger']*100:.2f}% гнева/злости (anger),
        🤡 - {server_answer.json()['emotions']['fear']*100:.2f}% страха (fear),
        🤡 - {server_answer.json()['emotions']['sadness']*100:.2f}% грусти/печали (sadness),
        🤡 - {server_answer.json()['emotions']['enthusiasm']*100:.2f}% удивления/энтузиазма (enthusiasm),
        🤡 - {server_answer.json()['emotions']['disgust']*100:.2f}% отвращения (disgust),
        🤡 - {server_answer.json()['emotions']['neutral']*100:.2f}% нейтрально (neutral).""")
    else:
        bot.reply_to(message, "Что-то пошло не так. Попробуй еще раз. Ну или напиши создателю, вся информация в описании бота.")


bot.polling()

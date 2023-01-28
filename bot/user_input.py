import sympy as sp
import telebot
from telebot import types
import telebot
from dotenv import load_dotenv
from os import environ

load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

ban_words = {'_', 'import', 'os', 'requests', 'assert', 'eval'}


@bot.message_handler(content_types=['text'])
def input_check(message):
    try:
        x = sp.symbols('x')
        expression = message.text.split()
        for val in ban_words:
            if val in message.text:
                raise ValueError('Выражение содержит запрещенные слова')

    except Exception as e:
        if type(e) == NameError:
            bot.send_message(message.chat.id, 'Введено неправильное выражение')
        if type(e) == ValueError:
            bot.send_message(message.chat.id, e)
        else:
            bot.send_message(message.chat.id, 'Неизвестная ошибка. Повторите попытку')
            print(e)

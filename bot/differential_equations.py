import sympy as sp
from sympy import *
import telebot
from dotenv import load_dotenv
from os import environ

load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

# Присваивание символов переменным для дальнейших математических вычислений
x = sp.symbols('x')
y = sp.Function('y')


def differential_equation(x, y, message):
    """
    Параметр message содержит дифференциальное уравнение;
    Возвращает значение дифференциального уравнения
    """
    eq = diff(y(x), x) - eval(message.text)
    differ = sp.dsolve(eq, y(x)).simplify()
    bot.send_message(message.chat.id, differ)


def cauchy_problem(message):
    """
    Параметр message содержит дифференциальное уравнение, а также параметры x и y;
    Возвращает решение задачи Коши для заданного начального условия
    """
    expressions = message.text.split()
    integrate = expressions[0]
    answer1 = sp.dsolve(sp.integrate, y(x))

    bot.send_message(message.chat.id, answer1)



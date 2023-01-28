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


def derivative(message, point=False):
    """
    Параметр message содержит функцию и порядок производной
    Параметр point по умолчанию False. Если необходимо найти производную в точке, в параметре message
    также указана необходимая точка.
    Возвращает производную функции
    """
    expression = message.text.split()
    diff = sp.diff(expression[0], x, expression[1])
    if point:
        diff = sp.diff(expression[0], x, expression[1]).subs(x, expression[2])
    bot.send_message(message.chat.id, diff)


def tangent_equation(message):
    """
    Параметр message содержит заданную функцию и точку, к которой необходимо провести касательную;
    Возвращает уравнение касательной
    """
    expression = message.text.split()
    answer = tangent(eval(expression[0]), int(expression[1])).equation()
    bot.send_message(message.chat.id, answer)


def identifical_derivative(x, y, message):
    """
    Параметр message содержит функцию и порядок производной;
    Возвращает производную неявной функции
    """
    expression = message.text.split()
    idiff = sp.idiff(expression[0], x, y, expression[1])
    bot.send_message(message.chat.id, idiff)


def indefinite_integral(message):
    """
    Параметр message содержит подынтегральную функцию;
    Возвращает решение неопределенного интеграла
    """
    expression = message.text
    integrate = sp.integrate(expression, x)
    bot.send_message(message.chat.id, integrate)


def definite_integral(message):
    """
    Параметр message содержит подынтегральную функцию;
    Возвращает значение определенного интеграла
    """
    expressions = message.text.split()
    integrate = sp.integrate(expressions[0], (x, expressions[1], expressions[2]))
    bot.send_message(message.chat.id, integrate)

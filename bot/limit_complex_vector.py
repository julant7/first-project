import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import *
import telebot
from telebot import types
from dotenv import load_dotenv
from os import environ, cpu_count

load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

# Присваивание символов переменным для дальнейших математических вычислений
x = sp.symbols('x')
y = sp.Function('y')


def limit_calculation(message):
    """
    Параметр message содержит выражение для вычисления предела: функцию, предел величины и указание
    левый/правый предел (третий аргумент не обязателен)
    Возвращает значения предела
    """
    expressions = message.text.split()
    if len(expressions) == 3:
        answer = sp.limit(expressions[0], expressions[1], expressions[2], dir='+-')
    else:
        answer = sp.limit(expressions[0], expressions[1], expressions[2], dir=expressions[3])
    bot.send_message(message.chat.id, answer)


def quadratic_equation_roots(message):
    """
    Параметр message содержит уравнение, содержащее комплексные числа/предполагающее ответ с комплексными числами;
    Возвращает решение уравнения
    """
    i = complex(0, 1)
    exposed_methods = {'cpu_count': cpu_count}
    solution = solve(eval(message.text, {'__builtins__': None}, exposed_methods))
    for answers in solution:
        bot.send_message(message.chat.id, f'{solution.index(answers) + 1} корень: {answers}')


def cross_product(message):
    """
    Параметр message содержит координаты векторов, а также их размерность;
    Возвращает значение произведения двух векторов
    """
    coordinates = message.text.split()
    for i, element in enumerate(coordinates):
        coordinates[i] = int(element)
    index_first_array = coordinates[len(coordinates) - 2]
    index_second_array = coordinates[len(coordinates) - 1]
    first_vector = []
    second_vector = []
    for index in range(index_first_array):
        first_vector.append(coordinates[index])
    for index in range(index_second_array, len(coordinates) - 2):
        second_vector.append(coordinates[index])
    first_vector = np.array(first_vector)
    second_vector = np.array(second_vector)
    answer = np.cross(first_vector, second_vector)
    bot.send_message(message.chat.id, answer)


def plotting(message):
    """
    Построение графика с фиксированными значениями;
    Возвращает построенный график в формате png
    """
    fig = plt.figure()
    x = np.linspace(-2, 2, 500)
    # В узкий интервал около нуля записываем значения NaN
    x[(x > -0.01) & (x < 0.01)] = np.nan  # определить промежутки
    y = np.arctan(1 / x)
    plt.plot(x, y, color='cyan')
    ax = plt.gca()
    ax.set_facecolor('lightpink')
    plt.vlines(0, -1.6, 1.6, color='magenta', linestyles='dashed')
    fig.savefig('files/saved_figure.png')
    with open('files/saved_figure.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk as mpl
import telebot
from dotenv import load_dotenv
from os import environ

load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

plt.style.use("cyberpunk")
fig = plt.figure()


@bot.message_handler(content_types=['text'])
def circle(message):
    """
    Построение окружности
    Параметр message содержит выбранный радиус фигуры;
    Возвращает построенный график
    """
    r = int(message.text)
    t = np.arange(0, 2*np.pi, 0.01)
    x = r*np.sin(t)
    y = r*np.cos(t)
    plt.plot(x, y, lw=2, color="darkviolet")
    plt.axis('equal')

    mpl.add_glow_effects()

    fig.savefig('files/saved_figure.png')
    with open('files/saved_figure.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def ellipse(message):
    """
    Построение эллипса
    Параметр message содержит выбранные значения большой и малой полуосей;
    Возвращает построенный график
    """
    semi_axes = message.text.split()
    a = int(semi_axes[0])
    b = int(semi_axes[1])
    t = np.arange(0, 2*np.pi, 0.01)
    x = a*np.sin(t)
    y = b*np.cos(t)
    plt.plot(x, y, lw=2, color="mediumorchid")
    mpl.add_glow_effects()

    fig.savefig('files/saved_figure.png')
    with open('files/saved_figure.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def parabola(message):
    """
    Построение параболы
    Параметр message содержит выбранное значение параметра p;
    Возвращает построенный график
    """
    parameter = int(message.text)
    if parameter > 0:
        x = np.linspace(0, 100, 100)
    else:
        x = np.linspace(-100, 0, 100)
    y1 = np.sqrt(2*x*parameter)
    y2 = -np.sqrt(2*x*parameter)

    plt.plot(x, y1, lw=2, color="aqua")
    plt.plot(x, y2, lw=2, color='gold')

    plt.grid(True, linestyle='-', color='0.4')
    mpl.add_glow_effects()

    fig.savefig('files/saved_figure.png')
    with open('files/saved_figure.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


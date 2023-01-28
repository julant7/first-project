import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import mplcyberpunk as mpl
import telebot
from dotenv import load_dotenv
from os import environ

load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

plt.style.use("cyberpunk")


@bot.message_handler(content_types=['text'])
def ellipsoid(message):
    """
    Построение эллипсоида;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(projection='3d')

    # Коэффициенты уравнения
    coefs = (1, 2, 2)
    # Радиусы, соответствующие коэффициентам
    rx, ry, rz = 1/np.sqrt(coefs)

    # Сферические углы
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    # Уравнение эллипсоида
    x = rx*np.outer(np.cos(u), np.sin(v))
    y = ry*np.outer(np.sin(u), np.sin(v))
    z = rz*np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z, rstride=4, cstride=4)

    mpl.add_glow_effects()

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def single_cavity_hyperboloid(message):
    """
    Построение однополостного гиперболоида;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(projection='3d')

    u = np.linspace(-2, 2, 200)
    v = np.linspace(0, 2*np.pi, 60)
    [u, v] = np.meshgrid(u, v)

    x = np.cosh(u)*np.cos(v)
    y = np.cosh(u)*np.sin(v)
    z = np.sinh(u)

    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='blueviolet')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def double_cavity_hyperboloid(message):
    """
    Построение двуполостного гиперболоида;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(progection='3d')

    x = np.linspace(-3, 3, 500)
    y = np.linspace(-3, 3, 500)
    [x, y] = np.meshgrid(x, y)
    z1 = lambda w: np.sqrt(w[0]**2 + w[1]**2 + 1)
    Z1 = z1((x, y))
    z2 = lambda w: -np.sqrt(w[0]**2 + w[1]**2 + 1)
    Z2 = z2((x, y))

    ax.plot_surface(x, y, Z1, rstride=4, cstride=4, color='r')
    ax.plot_surface(x, y, Z2, rstride=4, cstride=4, color='r')

    plt.show()

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def cone(message):
    """
    Построение конуса;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2*np.pi, 100)
    r = np.linspace(-1, 1, 100)
    t, R = np.meshgrid(theta, r)

    x = R*np.cos(t)
    y = R*np.sin(t)
    z1 = R
    z2= -R

    ax.plot_surface(x, y, z1, color='y')
    ax.plot_surface(x, y, z2, color='y')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

def elliptical_paraboloid(message):
    """
    Построение эллиптического параболоида;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(projection='3d')

    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    [x, y] = np.meshgrid(x, y)

    z = lambda w: w[0]**2 + w[1]**2
    Z = z((x, y))

    ax.plot_surface(x, y, Z, rstride=4, cstride=4, color='palegreen')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def hyperbolic_paraboloid(message):
    """
    Построение эллипсоида;
    Возвращает 3D-график гиперболического параболоида
    """
    f = lambda x, y: x**2 - y**2
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    xval = np.linspace(-4, 4, 100)
    yval = np.linspace(-4, 4, 100)
    x, y = np.meshgrid(xval, yval)
    z = f(x, y)

    ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap=cm.plasma)

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def elliptical_cylinder(message):
    """
    Построение эллиптического цилиндра;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-1, 1, 100)
    z = np.linspace(0, 3, 100)
    x, z = np.meshgrid(x, z)

    y = np.sqrt(1-x**2)
    ax.plot_surface(x, y, color='b')
    ax.plot_surface(x, -y, z, color='b')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def hyperbolic_cylinder(message):
    """
    Построение гиперболического цилиндра;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-5, 5, 100)
    z = np.linspace(0, 3, 100)
    x, z = np.meshgrid(x, z)

    y = np.sqrt(10+x**2)
    ax.plot_surface(x, y, z, color='g')
    ax.plot_surface(x, -y, z, color='g')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def parabolic_cylinder(message):
    """
    Построение параболического цилиндра;
    Возвращает 3D-график поверхности
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(0, 1, 100)
    z = np.linspace(0, 3, 100)
    x, z = np.meshgrid(x, z)

    y = np.sqrt(2*x)
    ax.plot_surface(x, y, z, color='r')
    ax.plot_surface(x, -y, z, color='r')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def intersecting_planes(message):
    """
    Построение пересекающихся плоскостей;
    Возвращает получившийся 3D-график
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-1, 1, 100)
    z = np.linspace(0, 3, 100)
    x, z = np.meshgrid(x, z)
    y = x

    ax.plot_surface(x, y, z, color='g')
    ax.plot_surface(x, -y, z, color='g')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def parallel_planes(message):
    """
    Построение параллельных плоскостей;
    Возвращает получившийся 3D-график
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(0, 1, 100)
    z = np.linspace(0, 3, 100)
    x, z = np.meshgrid(x, z)
    y = 2

    ax.plot_surface(x, y, z, color='g')
    ax.plot_surface(x, -y, z, color='g')

    fig.savefig('files/saved_surface.png')
    with open('files/saved_surface.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

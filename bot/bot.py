from differential_equations import differential_equation, cauchy_problem
from derivative_and_integrals import derivative, tangent_equation, identifical_derivative, indefinite_integral, definite_integral
from limit_complex_vector import limit_calculation, quadratic_equation_roots, cross_product, plotting
from second_order_surfaces import ellipsoid, elliptical_paraboloid, hyperbolic_paraboloid, single_cavity_hyperboloid,\
    double_cavity_hyperboloid, cone, elliptical_cylinder, hyperbolic_cylinder, parabolic_cylinder, intersecting_planes,\
    parallel_planes
from second_order_curves import circle, ellipse, parabola

from dotenv import load_dotenv
from os import environ
import sympy as sp
import telebot
from telebot import types


load_dotenv()
bot = telebot.TeleBot(environ.get('API_KEY'))

# Присваивание символов переменным для дальнейших математических вычислений
x = sp.symbols('x')
y = sp.Function('y')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Производная')
    btn2 = types.KeyboardButton('Интегралы')
    btn3 = types.KeyboardButton('Дифференциальные уравнения')
    btn4 = types.KeyboardButton('Аналитическая геометрия')
    btn5 = types.KeyboardButton('Предел')
    btn6 = types.KeyboardButton('Комплексные числа')
    btn7 = types.KeyboardButton('Построение графика')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    mess = f'Начните использовать бот с помощью меню'
    bot.send_message(message.chat.id, mess, reply_markup=markup)


@bot.message_handler(commands=['surface'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классификация поверхностей в зависимости от значений инвариантов:')
    with open('../files/Поверхности второго порядка.pdf', 'rb') as document:
        bot.send_document(message.chat.id, document)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    match message.text.casefold():
        case 'производная':
            btn1 = types.KeyboardButton('Производная n-ого порядка')
            btn2 = types.KeyboardButton('Уравнение касательной')
            btn3 = types.KeyboardButton('Значение производной в точке')
            btn4 = types.KeyboardButton('Производная неявной функции')
            btn5 = types.KeyboardButton('Вернуться')
            markup = types.ReplyKeyboardMarkup()
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, 'Выберите тип задачи', reply_markup=markup)

        case 'интегралы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Неопределенный интеграл')
            btn2 = types.KeyboardButton('Определенный интеграл')
            btn3 = types.KeyboardButton('Вернуться')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Выберите тип интеграла', reply_markup=markup)

        case 'дифференциальные уравнения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Уравнения первого порядка')
            btn2 = types.KeyboardButton('Задача Коши')
            btn3 = types.KeyboardButton('Вернуться')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, 'Выберите тип задачи', reply_markup=markup)

        case 'аналитическая геометрия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Произведение 2-ух векторов')
            btn2 = types.KeyboardButton('Поверхности 2-ого порядка')
            btn3 = types.KeyboardButton('Кривые 2-ого порядка')
            btn4 = types.KeyboardButton('Вернуться')
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, 'Выберите тип задачи', reply_markup=markup)

        case 'предел':
            msg = bot.reply_to(message, 'Введите предел')
            bot.register_next_step_handler(msg, limit_calculation)

        case 'построение графика':
            msg = bot.reply_to(message, 'Скажите, как у вас дела')
            bot.register_next_step_handler(msg, plotting)

        case 'комплексные числа':
            msg = bot.reply_to(message, 'Введите уравнение')
            bot.register_next_step_handler(msg, quadratic_equation_roots)

        case 'производная n-ого порядка':
            msg = bot.reply_to(message, 'Введите функцию и порядок производной через пробел')
            bot.register_next_step_handler(msg, derivative)

        case 'уравнение касательной':
            msg = bot.reply_to(message, 'Введите функцию и точку')
            bot.register_next_step_handler(msg, tangent_equation)

        case 'значение производной в точке':
            msg = bot.reply_to(message, 'Введите выражение, порядок и точку через пробел')
            bot.register_next_step_handler(msg, derivative(message, point=True))

        case 'производная неявной функции':
            msg = bot.reply_to(message, 'Введите функцию и порядок производной через пробел')
            bot.register_next_step_handler(msg, identifical_derivative)

        case 'неопределенный интеграл':
            msg = bot.reply_to(message, 'Введите подынтегральную функцию')
            bot.register_next_step_handler(msg, indefinite_integral)

        case 'определенный интеграл':
            msg = bot.reply_to(message, 'Введите подынтегральную функцию')
            bot.register_next_step_handler(msg, definite_integral)

        case 'уравнения первого порядка':
            msg = bot.reply_to(message, 'Введите дифференциальное уравнение')
            bot.register_next_step_handler(msg, differential_equation(x, y, msg))

        case 'задача коши':
            msg = bot.reply_to(message, 'Введите дифференциальное уравнение, параметры x и y')
            bot.register_next_step_handler(msg, cauchy_problem)

        case 'произведение 2-ух векторов':
            msg = bot.reply_to(message, 'Введите координаты векторов, а также размерность векторов через пробел')
            bot.register_next_step_handler(msg, cross_product)

        case 'поверхности 2-ого порядка':
            msg = bot.reply_to(message, 'Введите название поверхности')
            bot.register_next_step_handler(msg, surface_choice)

        case 'кривые 2-ого порядка':
            msg = bot.reply_to(message, 'Введите название кривой')
            bot.register_next_step_handler(msg, curves_choice)

        case 'вернуться':
            start(message)

        case _:
            bot.send_message(message.chat.id, 'Что-то пошло не так')


@bot.message_handler(content_types=['sticker', 'document', 'video', 'photo'])
def get_user_sticker(message):
    """Отправка стикера в ответ на стикер/документ/видео/фото"""
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEFjEpi91TDIgMm5XuTCAxalOqVlaUYfAAC6wMAAlojPQvLK1_UQSTH5ykE')


def curves_choice(message):
    """
    Построение кривых второго порядка
    """
    match message.text.casefold():
        case 'окружность':
            msg = bot.reply_to(message, 'Введите радиус окружности')
            bot.register_next_step_handler(msg, circle)
        case 'эллипс':
            msg = bot.reply_to(message, 'Введите значения большой и малой полуосей')
            bot.register_next_step_handler(msg, ellipse)
        case 'парабола':
            msg = bot.reply_to(message, 'Введите величину параметра p')
            bot.register_next_step_handler(msg, parabola)
        case _:
            bot.send_message(message.chat.id, 'Что-то пошло не так')


def surface_choice(message):
    """
    Параметр message содержит название выбранной поверхности
    При правильно введенном названии вызывает функцию построения поверхности
    """
    match message.text.casefold():
        case 'эллипсоид':
            ellipsoid(message)
        case 'однополостный гиперболоид':
            single_cavity_hyperboloid(message)
        case 'двуполостный гиперболоид':
            double_cavity_hyperboloid(message)
        case 'конус':
            cone(message)
        case 'эллиптический параболоид':
            elliptical_paraboloid(message)
        case 'гиперболический параболоид':
            hyperbolic_paraboloid(message)
        case 'эллиптический цилиндр':
            elliptical_cylinder(message)
        case 'гиперболический цилиндр':
            hyperbolic_cylinder(message)
        case 'параболический цилиндр':
            parabolic_cylinder(message)
        case 'пара пересекающихся плоскостей' | 'пересекающиеся плоскости':
            intersecting_planes(message)
        case 'пара параллельных плоскостей' | 'параллельные плоскости':
            parallel_planes(message)
        case _:
            bot.send_message(message.chat.id, 'Что-то пошло не так')


if __name__ == "__main__":
    bot.polling(none_stop='True')

import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6232866768:AAEs6wotHDIU5EjMgOmx3fMunBApj-PpIS8')


# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Аутентификация", callback_data='auth'))

    bot.send_message(message.chat.id, "Привет✌️, Сейчас вы пройдете этап идентификации для входа в 15 модуль.", reply_markup=markup)


# Функция для обработки inline-клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "auth":
        bot.answer_callback_query(call.id)

        # Запрашиваем ФИО
        bot.send_message(call.message.chat.id, "Введите свое ФИО:")
        bot.register_next_step_handler(call.message, get_name)


def get_name(message):
    # Сохраняем ФИО в переменной и запрашиваем должность
    name = message.text
    bot.send_message(message.chat.id, "Введите свою должность:")
    bot.register_next_step_handler(message, get_position, name)


def get_position(message, name):
    # Сохраняем должность в переменной и запрашиваем кабинет
    position = message.text
    bot.send_message(message.chat.id, "Введите свой кабинет:")
    bot.register_next_step_handler(message, get_room, name, position)


def get_room(message, name, position):
    # Сохраняем кабинет в переменной и выводим сообщение об успешной аутентификации
    room = message.text
    bot.send_message(message.chat.id, "Аутентификация пройдена успешно! Ваше ФИО: {0}, должность: {1}, кабинет: {2}".format(name, position, room))


bot.polling()


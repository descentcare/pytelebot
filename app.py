from config import TOKEN
import telebot 
from telebot.types import (
        ReplyKeyboardMarkup, 
        KeyboardButton,
        InlineKeyboardMarkup,
        InlineKeyboardButton,
        )
bot = telebot.TeleBot(TOKEN, parse_mode = None)

menu0 = (
        "Схема расположения",
        "Транспорт + контакт",
        "Партнеры",
        "Обратная связь",
        "Covid",
        "Программа",
        )
markup0 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markup0.add(*(KeyboardButton(x) for x in menu0))

menu1 = (
        "Корпуса",
        "Беседки 0 день",
        "В главное меню",
        )
markup1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markup1.add(*(KeyboardButton(x) for x in menu1))

@bot.message_handler(func = lambda message: message.text == "Программа")
def program_message(message):
    bot.send_message( message.chat.id,
            "Программа на сегодняший вечер:",
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Схема расположения")
def schemes_message(message):
    bot.send_message(message.chat.id,
            "Выбор схем расположения",
            reply_markup = markup1)

@bot.message_handler(func = lambda message: message.text == "Корпуса")
def blocks_message(message):
    bot.send_photo(message.chat.id, open('img/rd.jpg', 'rb'), 
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Беседки 0 день")
def gazebos_message(message):
    bot.send_photo(message.chat.id, open('img/rdg.jpg', 'rb'), 
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Транспорт + контакт")
def contacts_message(message):
    bot.send_message(message.chat.id,
            "Ваши Транспорт + контакт",
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Партнеры")
def partners_message(message):
    bot.send_message(message.chat.id,
            "Наши Партнеры",
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Обратная связь")
def partners_message(message):
    bot.send_message(message.chat.id,
            "Способы до нас достучаться:",
            reply_markup = markup0)

@bot.message_handler(func = lambda message: message.text == "Covid")
def partners_message(message):
    bot.send_message(message.chat.id,
            "Информация по коронавирусу: ",
            reply_markup = markup0)

@bot.message_handler(commands=["start"])
@bot.message_handler(func = lambda message: message.text == "В главное меню")
@bot.message_handler(func=lambda message: message.text not in menu0+menu1)
def all_messages(message):
    bot.send_message(message.chat.id, "Что ты хочешь узнать?", reply_markup=markup0)

bot.infinity_polling()

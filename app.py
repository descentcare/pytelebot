from config import TOKEN
import telebot
from telebot.types import (
        ReplyKeyboardMarkup, 
        KeyboardButton,
        InlineKeyboardMarkup,
        InlineKeyboardButton,
        )
bot = telebot.TeleBot(TOKEN, parse_mode = None)

markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

menu = {
        "Программа": lambda chat_id: bot.send_message(chat_id, "Текст в ответ на Программа"),
        "Схема расположения корпусов": lambda chat_id: bot.send_photo(chat_id, open("img/rd.jpg", 'rb')),
        "Схема расположения беседок 0 день": lambda chat_id: bot.send_message(chat_id, "asdlf"),
        "Транспорт + контакт": lambda chat_id: bot.send_message(chat_id, "erq"),
        "Партнеры": lambda chat_id: bot.send_message(chat_id, "ewqr"),
        "Обратная связь": lambda chat_id: bot.send_message(chat_id, ",cxmzn"),
        "Covid": lambda chat_id: bot.send_message(chat_id, "gdsajlksdm"),
    }
buttons = [KeyboardButton(x) for x in menu]
markup.add(*buttons)
'''
markup = InlineKeyboardMarkup()
markup.row_width = 2
markup.add(*(InlineKeyboardButton(menu_text[i], callback_data=f'cd_{i}')
    for i in range(len(menu_text))
    ))

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.send_message(call.message.chat.id, 'sadfasdf', reply_markup=markup)

@bot.message_handler(commands=["start"])
def inl_message(message):
    bot.send_message(message.chat.id, "adfs", reply_markup=markup)
'''
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!", reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    menu[message.text](message.chat.id)
    bot.send_message(message.chat.id, "Что ты хочешь узнать?", reply_markup=markup)

bot.infinity_polling()

from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def roll_markup():
    make_num = KeyboardButton(text="Дай число")
    close_keyboard = KeyboardButton(text="Выйти")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(make_num,close_keyboard)
    return keyboard

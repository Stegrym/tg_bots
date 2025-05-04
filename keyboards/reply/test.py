from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def gen_markup():
    button_roll = KeyboardButton(text="Сгенерировать число")
    button_take_num = KeyboardButton(text="Выбрать число")
    button_exit = KeyboardButton(text="Закрыть генератор")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_roll, button_take_num, button_exit)
    return keyboard

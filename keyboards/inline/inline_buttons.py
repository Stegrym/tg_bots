from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def inline_buttons():
    button_1 = InlineKeyboardButton(text="1", callback_data="кнопка один")
    button_2 = InlineKeyboardButton(text="1", callback_data="кнопка два")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_1,button_2)
    return keyboard
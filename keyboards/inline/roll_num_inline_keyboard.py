from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def markup():
    roll_button = InlineKeyboardButton(text="Roll", callback_data="roll_num_inline")
    exit_button = InlineKeyboardButton(text="Exit", callback_data="exit_roll_num_inline")
    option_button = InlineKeyboardButton(text="Option", callback_data="change_roll_num_inline")

    keyboard = InlineKeyboardMarkup()
    keyboard.row(roll_button, exit_button)
    keyboard.row(option_button)
    return keyboard

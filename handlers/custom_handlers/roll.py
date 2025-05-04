from loader import bot
from random import randint
from keyboards.reply import roll_keyboard
from telebot.types import Message, ReplyKeyboardRemove


@bot.message_handler(commands=["roll"])
def roll_start(message: Message):
    """Ролит число"""
    bot.send_message(
        chat_id=message.from_user.id,
        text="Генератор случайных чисел запущен\nвыберете действие",
        reply_markup=roll_keyboard.roll_markup(),
    )


@bot.message_handler(func=lambda message: message.text == "Дай число")
def take_num(message: Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"{randint(1, 10)}",
    )

@bot.message_handler(func=lambda message: message.text == "Выйти")
def close_roll(message:Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text="Генератор закрыт",
        reply_markup=ReplyKeyboardRemove(),
    )

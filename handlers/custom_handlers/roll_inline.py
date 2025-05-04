from loader import bot
import random
from keyboards.inline import roll_num_inline_keyboard
from telebot.types import Message


@bot.message_handler(commands=["random"])
def roll_inline(message: Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text="Запускаю генератор чисел\n"
             "Выберете действие",
        reply_markup=roll_num_inline_keyboard.markup()
    )


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "roll_num_inline":
        bot.edit_message_reply_markup(callback.from_user.id, callback.message.message_id)
        bot.send_message(callback.from_user.id, f"Число {random.randint(1, 10)}",
                         reply_markup=roll_num_inline_keyboard.markup())
        bot.delete_message(callback.from_user.id, message_id=callback.message.message_id)
    elif callback.data == "exit_roll_num_inline":
        bot.edit_message_reply_markup(callback.from_user.id, callback.message.message_id)
        bot.send_message(callback.from_user.id, f"Рандомайзер закрыт")

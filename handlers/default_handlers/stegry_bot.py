from loader import bot
from telebot.types import Message

@bot.message_handler(commands=["stegrybot"])
def call_bot(message:Message):
    bot.send_message(
        chat_id=message.from_user.id,
        text=f"Привет,{message.from_user.full_name}\n"
             f"Выберите из списка, что я могу для вас сделать?"
    )

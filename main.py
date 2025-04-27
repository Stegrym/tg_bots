import telebot
import os

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, "START!")


bot.infinity_polling()

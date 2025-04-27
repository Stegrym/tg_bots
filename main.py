import telebot
import os

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(commands=["start"])
def start_message(message: telebot.types.Message):
    # parse_mode="html" - даёт возможность форматировать текст на языке html
    bot.send_message(message.from_user.id, "<b>START!</b>", parse_mode="html")


@bot.message_handler()
def info(message: telebot.types.Message):
    if message.text.lower() == "id":
        bot.reply_to(message, f"{message.from_user.id}")


bot.infinity_polling()

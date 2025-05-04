from telebot.types import Message

from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    """Выводит на экран список всех команд с описанием из
    config.DEFAULT_COMMANDS"""
    text = [f"/{command} - {info}" for command, info in DEFAULT_COMMANDS]
    bot.send_message(message.from_user.id, "<b>Список доступных команд:</b>\n" + "\n".join(text), parse_mode='html')

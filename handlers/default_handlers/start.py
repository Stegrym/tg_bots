from loader import bot
from config_data.config import DEFAULT_COMMANDS
from telebot.types import Message


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    commands_list = [f"/{command} - {info}" for command, info in DEFAULT_COMMANDS]
    bot.send_message(
        message.from_user.id,
        f"<b>Приветствую, {message.from_user.full_name}\n\n"
        f"Вот список команд:</b>\n"
        + "\n\t".join(commands_list),
        parse_mode="html",
    )

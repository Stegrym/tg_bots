import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены,\n отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KAY")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = (
    ("help", "Список команд"),
    ("roll", "Генератор случайных чисел"),
    ("random","Генерация с кнопками")
    # ("stegrybot", "Позвать бота"),

)


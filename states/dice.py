from telebot.handler_backends import State, StatesGroup

class Dice(StatesGroup):
    start_number = State()
    end_number = State()


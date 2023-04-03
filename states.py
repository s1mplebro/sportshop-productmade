from aiogram.dispatcher.filters.state import StatesGroup, State 

class Reply(StatesGroup):
    username = State()
    user_reply = State()

class Location(StatesGroup):
    geo = State()

class Phone(StatesGroup):
    phone_number = State()

class Send(StatesGroup):
    text = State()
    photo  = State()

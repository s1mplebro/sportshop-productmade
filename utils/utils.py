from aiogram import types
from aiogram.dispatcher import FSMContext


async def get_changed_state(state: FSMContext, message: types.Message, field_name: str):
    async with state.proxy() as data:
        data[field_name] = message.text
        return data
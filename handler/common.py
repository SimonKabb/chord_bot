import os

from aiogram import types, Dispatcher

from image import tab_view
from varriable import TOKEN
from create_bot import dp, bot


# @dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "test"
    image = open(tab_view('Am'), 'rb')
    await bot.send_message(chat_id=chat_id, text=text)
    await bot.send_photo(chat_id=chat_id, photo=image)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(get_message)

import os

from aiogram import Dispatcher, types
from create_bot import dp, bot
from varriable import TOKEN


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "привет")
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

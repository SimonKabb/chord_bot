import logging
import sqlite3

from add_circles import make_chord
from aiogram import Dispatcher, types
from create_bot import bot


logging.basicConfig(level=logging.INFO, filename='main.log', filemode='w')


def find_chord(request):
    """searches the database for a string with the desired chord"""
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    request = request.upper()
    sqlite_select_query = (
        f"SELECT chord, positions, first_fing, img_type, lad FROM {request} WHERE name = '{request}'")
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    return records


async def get_message(message: types.Message):
    chat_id = message.chat.id
    logging.info(f'Сообщение {message.text} получено из {chat_id}')
    img_chords = find_chord(message.text)
    if len(img_chords):
        for one_chord in img_chords:
            chord = one_chord[0]
            positions = one_chord[1].split('s')
            first_fing = one_chord[2].split('s')
            img_type = one_chord[3]
            if one_chord[4]:
                lad = str(one_chord[4])
            else:
                lad = ''
            image = open(make_chord(
                positions,
                img_type=img_type,
                chord=chord,
                first_fing=first_fing,
                lad=lad), 'rb')
            await bot.send_photo(chat_id=chat_id, photo=image)
    else:
        await bot.send_message(chat_id=chat_id,
                               text='Я еще такого аккорда не знаю')
        logging.error(f'Аккорда {message.text} нет в БД')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(get_message)

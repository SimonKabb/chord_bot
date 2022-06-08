from add_circles import make_chord
from aiogram import Dispatcher, types
from create_bot import bot
import sqlite3
# @dp.message_handler()


def find_chord(request):
    """searches the database for a string with the desired chord"""
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    request = request.upper()
    sqlite_select_query = (
        f"SELECT chord, positions, first_fing, img_type, type FROM {request[0]} WHERE name = '{request}'")
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    print(records)
    return records


async def get_message(message: types.Message):
    chat_id = message.chat.id
    img_chords = find_chord(message.text)
    for y in img_chords:
        chord = y[0]
        positions = y[1].split('P')
        first_fing = y[2].split()
        img_type = y[3]
        image = open(make_chord(positions, img_type=img_type,
                                chord=chord, first_fing=first_fing), 'rb')
        await bot.send_photo(chat_id=chat_id, photo=image)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(get_message)

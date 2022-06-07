from add_circles import make_chord
from aiogram import Dispatcher, types
from create_bot import bot
import sqlite3
# @dp.message_handler()


def find_chord(request):
    """searches the database for a string with the desired chord"""
    sqlite_connection = sqlite3.connect('handler/chords.db')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = (
        f"SELECT tab FROM {request[0].upper()} WHERE name = '{request.upper()}'")
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    return records


async def get_message(message: types.Message):
    chat_id = message.chat.id
    img_chords = find_chord(message.text)
    for img_chord in img_chords:
        print(*img_chord)
        image = open(make_chord(*img_chord), 'rb')
        await bot.send_photo(chat_id=chat_id, photo=image)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(get_message)

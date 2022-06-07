import sqlite3


def find_chord(request):
    sqlite_connection = sqlite3.connect('handler/chords.db')
    cursor = sqlite_connection.cursor()
    request = request.upper()
    sqlite_select_query = f"SELECT tab FROM {request[0].upper()} WHERE name='{request}'"
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    print(records)


find_chord('am')

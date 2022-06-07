import sqlite3

sqlite_connection = sqlite3.connect('chords.db')
cursor = sqlite_connection.cursor()
"""table create"""
# cursor.execute("""CREATE TABLE A(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     tab TEXT NOT NULL,
#     type TEXT,
#     image BLOB
# )
# """)
"""chord create"""
cursor.execute("""
            UPDATE A SET name = 'AM' WHERE id=1
            """)
sqlite_connection.commit()
sqlite_connection.close()

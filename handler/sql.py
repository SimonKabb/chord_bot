import sqlite3

sqlite_connection = sqlite3.connect('chords.db')
cursor = sqlite_connection.cursor()
"""table create"""
cursor.execute("""CREATE TABLE A(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    chord TEXT NOT NULL,
    positions TEXT,
    first_fing TEXT,
    img_type INTEGER,
    type TEXT,
    image BLOB
)
""")
"""chord create"""
cursor.execute("""
            INSERT INTO A (name, chord, positions, first_fing, img_type, type) VALUES("AM", "Am", "2x4P3x3","1x2",1,"minor")
            """)


# """chord rename"""
# cursor.execute("""
#             UPDATE A SET name = 'AM' WHERE id=1
#             """)
sqlite_connection.commit()
sqlite_connection.close()

import sqlite3

sqlite_connection = sqlite3.connect('chords.db')
cursor = sqlite_connection.cursor()
# """table create"""
# cursor.execute("""CREATE TABLE G(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     chord TEXT NOT NULL,
#     positions TEXT,
#     first_fing TEXT,
#     img_type INTEGER,
#     lad INTEGER,
#     type TEXT,
#     image BLOB
# )
# """)
# """table delete"""
# cursor.execute("""DROP TABLE С;
# """)
"""chord create"""
cursor.execute("""
            INSERT INTO E (name, chord, positions, first_fing, img_type, lad, type) VALUES("EM", "Em", "2x5P3x4","",1,"","minor")
            """)


# """chord rename"""
# cursor.execute("""
#             UPDATE E SET chord = 'E' WHERE id=1
#             """)
sqlite_connection.commit()
sqlite_connection.close()

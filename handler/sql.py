import sqlite3

sqlite_connection = sqlite3.connect('chords.db')
cursor = sqlite_connection.cursor()
# """table create"""
# cursor.execute("""
#     CREATE TABLE AM(
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL REFERENCES main_chords (name),
#     first_fing TEXT,
#     positions TEXT,
#     img_type INTEGER,
#     lad INTEGER,
#     chord TEXT,
#     img BLOB
# )
# """)
# """table delete"""
# cursor.execute("""DROP TABLE AM;
# """)
# """make main_chord"""
# cursor.execute("""
#             INSERT INTO main_chords (name, tonic, scale) VALUES("G", "G", "major")
#             """)
# # """chord create"""
# cursor.execute("""
#             INSERT INTO AM (name, first_fing, positions, img_type, chord) VALUES ("AM", "1x2", "2x4s3x3", 1, "Am")
#             """)
"""chord create"""
cursor.execute("""
            INSERT INTO AM (name, first_fing, positions, img_type, chord, lad) VALUES ("AM", "1x1s1x2s1x3s1x5", "3x4s3x5", 2, "Am", 5)
            """)

# """chord rename"""
# cursor.execute("""
#             UPDATE AM SET first_fing = '1x1s1x2s1x3s1x6' WHERE id=2
#             """)
sqlite_connection.commit()
sqlite_connection.close()

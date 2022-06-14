import sqlite3


def create_table(chord):
    """table create"""
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""
            CREATE TABLE {chord}(
            id INTEGER PRIMARY KEY,
            main_id INTEGER NOT NULL REFERENCES main_chords (id),
            first_fing TEXT,
            positions TEXT,
            img_type INTEGER,
            lad INTEGER,
            chord TEXT,
            img BLOB
        )
        """)
    sqlite_connection.commit()
    sqlite_connection.close()


def table_delete(table):
    """table delete"""
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"DROP TABLE {table};")
    sqlite_connection.commit()
    sqlite_connection.close()


def delete_chord(table, id):
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""DELETE FROM {table}
                        WHERE id = {id}
                    """)
    sqlite_connection.commit()
    sqlite_connection.close()


def make_main_chord(name, tonic, scale):
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""
                        INSERT INTO main_chords (name, tonic, scale)
                        VALUES('{name}', '{tonic}', '{scale}')
                        """)
    sqlite_connection.commit()
    sqlite_connection.close()


def chord_create(table, first_fing, positions, img_type, chord, main_id, lad):
    """chord create"""
    sqlite_connection = sqlite3.connect('chords.db')
    cursor = sqlite_connection.cursor()
    cursor.execute(f"""
                INSERT INTO {table} 
                (first_fing, positions, img_type, chord, main_id,lad)
                VALUES ('{first_fing}',
                '{positions}',
                {img_type},
                '{chord}',
                '{main_id}',
                '{lad}');
                """)
    sqlite_connection.commit()
    sqlite_connection.close()


"""chord update"""
# cursor.execute("""
#             UPDATE AM SET first_fing = '1x1s1x2s1x3s1x6' WHERE id=2
#             """)

chord_create(table='D', first_fing='1x5', positions='3x2s3x3s3x4',
             img_type=2, chord='D', lad=5, main_id=5)
# delete_chord('CM', 1)
# make_main_chord('D', 'D', 'major')
# create_table('D')

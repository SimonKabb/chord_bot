from PIL import Image, ImageDraw, ImageFont
from constant_set import POSITON_CIRCLE
import sqlite3


class Chord:
    def __init__(self, *positions, first_fing, chord, img_type, lad=''):
        self.positions = positions,
        self.first_fing = first_fing,
        self.chord = chord,
        self.img_type = img_type,
        self.lad = lad

    def make_chord(self):
        if self.img_type == 1:
            im = Image.open('img_tabs/sample1.png')
        else:
            im = Image.open('img_tabs/sample2.png')
        draw = ImageDraw.Draw(im)
        for position in self.first_fing:
            coord_pos = POSITON_CIRCLE[position]
            draw.ellipse(coord_pos, 'white', 'black', width=3)
            font = ImageFont.truetype('fonts/Prompt-Medium.ttf', size=28)
            draw.text(
                (coord_pos[0]+18, coord_pos[1]+5),
                '1',
                fill=('#1C0606'),
                font=font
            )
        finger_number = 2
        for position in self.positions:
            coord_pos = POSITON_CIRCLE[position]
            draw.ellipse(coord_pos, 'white', 'black', width=3)
            font = ImageFont.truetype('fonts/Prompt-Medium.ttf', size=28)
            draw.text(
                (coord_pos[0]+18, coord_pos[1]+5),
                str(finger_number),
                fill=('#1C0606'),
                font=font
            )
            finger_number += 1
            draw.text(
                (10, 10),
                self.chord,
                fill=('#1C0606'),
                font=font
            )
            draw.text(
                (100, 300),
                self.lad,
                fill=('#1C0606'),
                font=font
            )
        # im.show()
        path = f'img_tabs/{self.chord}.png'
        im.save(path)

        return path


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
    if len(records):
        return records
    else:


x = find_chord('am')
for y in x:
    chord = y[0]
    positions = tuple(y[1].split('P'))
    first_fing = y[2]
    img_type = y[3]
    print(positions, img_type,
          chord, first_fing)

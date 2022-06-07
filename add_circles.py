from PIL import Image, ImageDraw, ImageFont
from constant_set import POSITON_CIRCLE


def make_chord(*positions, first_fing, chord, img_type, lad=''):
    """Сreates the position of the fingers on the image."""
    if img_type == 1:
        im = Image.open('img_tabs/sample1.png')
    else:
        im = Image.open('img_tabs/sample2.png')
    draw = ImageDraw.Draw(im)
    for position in first_fing:
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
    for position in positions:
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
            chord,
            fill=('#1C0606'),
            font=font
        )
        draw.text(
            (100, 300),
            lad,
            fill=('#1C0606'),
            font=font
        )
    # im.show()
    path = f'img_tabs/{chord}.png'
    im.save(path)
    return path


# make_chord('2x3', '2x1', '3x2', chord='D', img_type=1)
make_chord('2x4', '3x3',
           first_fing=['1x2'],
           chord='Am',
           img_type=1
           )

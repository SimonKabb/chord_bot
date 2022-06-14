from PIL import Image, ImageDraw, ImageFont
from constant_set import POSITON_CIRCLE


def make_chord(positions, first_fing, chord, img_type, lad):
    """Сreates the position of the fingers on the image."""
    font_main = ImageFont.truetype('fonts/Prompt-Medium.ttf', size=28)
    font_lad = ImageFont.truetype('fonts/Prompt-Medium.ttf', size=24)
    if img_type == 1:
        im = Image.open('img_tabs/sample1.png')
    else:
        im = Image.open('img_tabs/sample2.png')
    draw = ImageDraw.Draw(im)
    for position in first_fing:
        coord_pos = POSITON_CIRCLE[position]
        draw.ellipse(coord_pos, 'white', 'black', width=3)
        draw.text(
            (coord_pos[0]+18, coord_pos[1]+5),
            '1',
            fill=('#1C0606'),
            font=font_main
        )
    finger_number = 2
    draw.text(
        (110, 318),
        lad,
        fill=('#1C0606'),
        font=font_lad
    )
    for position in positions:
        cord_pos = POSITON_CIRCLE[position]
        draw.ellipse(cord_pos, 'white', 'black', width=3)
        draw.text(
            (cord_pos[0]+18, cord_pos[1]+5),
            str(finger_number),
            fill=('#1C0606'),
            font=font_main
        )
        finger_number += 1
        draw.text(
            (10, 10),
            chord,
            fill=('#1C0606'),
            font=font_main
        )
    path = f'img_tabs/{chord}.png'
    im.save(path)

    return path


# make_chord('2x3', '2x1', '3x2', chord='D', img_type=1)
make_chord(positions=['5x4'],
           img_type=1,
           chord='am',
           first_fing=['4x3'],
           lad='3')

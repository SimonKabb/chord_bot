from PIL import Image, ImageDraw, ImageFont


def tab_view(chord):
    im = Image.new('RGB', (500, 350), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.line((50, 50, 450, 50), fill='black', width=5)
    draw.line((50, 100, 450, 100), fill='black', width=5)
    draw.line((50, 150, 450, 150), fill='black', width=5)
    draw.line((50, 200, 450, 200), fill='black', width=5)
    draw.line((50, 250, 450, 250), fill='black', width=5)
    draw.line((50, 300, 450, 300), fill='black', width=5)

    #draw.line((50, 48, 50, 302), fill='black', width=10)
    draw.line((80, 48, 80, 302), fill='grey', width=5)
    draw.line((160, 48, 160, 302), fill='grey', width=5)
    draw.line((240, 48, 240, 302), fill='grey', width=5)
    draw.line((320, 48, 320, 302), fill='grey', width=5)
    draw.line((400, 48, 400, 302), fill='grey', width=5)

    fnt = ImageFont.truetype("fonts/prompt-Medium.ttf", 35)
    # draw.text((40, 0), text=chord, font=fnt, fill=(0, 0, 0, 128))
    path = f'img_tabs/{chord}.png'
    im.save(path)
    return path

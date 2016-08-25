import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont


def suoxiao():
    im = Image.open('test.jpg')
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    im.save('thumbnail.jpg', 'jpeg')


# suoxiao()

def mohu():
    im = Image.open('thumbnail.jpg')
    im2 = im.filter(ImageFilter.BLUR)
    im2.save('blur.jpg', 'jpeg')


# mohu()


def rnd_char():
    return chr(random.randint(65, 90))


def rnd_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def yanzhengma():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    font = ImageFont.truetype('/usr/share/fonts/truetype/tlwg/Waree.ttf', 36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rnd_color())

    for t in range(4):
        draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())

    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


yanzhengma()

# 生成随机验证码
import PIL.Image as image
import PIL.ImageDraw as draw
import PIL.ImageFont as imgfont
import random

font = imgfont.truetype(r"E:\钟静\pythonProject\Week3\image\font.ttf", 60)
w = 240
h = 120


def randchar():
    """生成随机字母"""
    return chr(random.randint(65, 90))


def b_color():
    """生成随机背景色"""
    return (random.randint(200, 255),
            random.randint(200, 255),
            random.randint(200, 255))


def f_color():
    """生成随机前景色（即字母的颜色）"""
    return (random.randint(60, 120),
            random.randint(60, 120),
            random.randint(60, 120))


def img():
    return image.new("RGB", (w, h), (255, 255, 255))


if __name__ == '__main__':
    img = img()
    image = draw.Draw(img)
    for x in range(w):
        for y in range(h):
            image.point((x, y), fill = b_color())
    for i in range(4):
        image.text((60 * i + 10, 30), text = randchar(), fill = f_color(), font = font)
    img.show()

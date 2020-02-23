"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/2/13 21:50
"""
from PIL import Image, ImageDraw, ImageFont

font_size = 8
text = "我喜欢你！"
img_path = "./ym.jpg"

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype(r'E:\PythonCode\Github\Python100\5星\表白\4\hy.ttf', font_size)


def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]


ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)


img_new.convert('RGB').save("./ym_save.jpeg")
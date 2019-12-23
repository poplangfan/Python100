"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/17 21:56
"""
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image

# 此处开启可以自定义形状图片，但是要在WordCloud（）里加上mask=mask
mask = np.array(Image.open("xx/timg1.jpg"))  # 照片路径
with open("梁实秋中短篇作品.txt", "rb") as f:  # 你的文本
    t = f.read()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = WordCloud(mask=mask,
                  font_path="E:/font/hy.ttf",  # 字体路径
                  max_words=150,  # 最大展示词数
                  background_color="white",  # 背景颜色，默认黑色
                  )
    w.generate(txt)
    w.to_file("梁实秋.png")

# -*- coding: utf-8 -*-
# 解析并生成政府工作报告词云
import jieba
import wordcloud
# from scipy.misc import imread

# 此处开启可以自定义背景图片，但是要在wordcloud.WordCloud（）里加上mask=mask
# mask = imread("timg.jpg")
with open("2019gov.txt", "rb") as f:
    t = f.read()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(font_path="E:/font/hy.ttf", max_words=100,
                            background_color="white", width=800, height=600)
    w.generate(txt)
    w.to_file("gov.png")

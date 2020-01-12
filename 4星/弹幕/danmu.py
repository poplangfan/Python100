"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/1/11 22:47
"""
import re
import requests
from fake_useragent import UserAgent
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def get_danmu():
    base_url = "https://www.bilibili.com/bangumi/play/ep288244"  # 所有的弹幕实际地址的cid在这里
    url = "https://api.bilibili.com/x/v1/dm/list.so?oid={}"  # 弹幕的实际地址
    headers = {'User-Agent': UserAgent().Chrome}
    resp = requests.get(base_url, headers=headers)
    cid_list = re.findall(r'"cid":(\d+?),"from":', resp.text)
    cnt = 0
    with open("danmu.txt", "w", encoding="utf-8") as f:
        for cid in cid_list:
            # if cnt < 2:  # 调试用
            resp = requests.get(url.format(cid), headers=headers)
            resp.encoding = "utf-8"
            danmu_list = re.findall(r'">(.+?)</d>', resp.text)
            for danmu in danmu_list:
                f.write(danmu + " ")
            f.write("\n")
            cnt += len(danmu_list)
        print(cnt)  # 打印总的弹幕数


def word():
    mask = np.array(Image.open("./timg2.jpg"))  # 照片路径
    with open("danmu.txt", "r", encoding='UTF-8') as f:
        t = f.read()
        w = WordCloud(mask=mask,
                      font_path="E:/font/hy.ttf",  # 字体路径
                      max_words=150,  # 最大展示词数
                      background_color="white",  # 背景颜色，默认黑色
                      collocations=False
                      )
        w.generate(t)
        w.to_file("./test.png")


if __name__ == '__main__':
    get_danmu()
    word()

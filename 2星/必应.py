"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/11/22 22:38
"""
import os
import requests
from lxml import etree
from fake_useragent import UserAgent


# 获取Bing美图
url = "https://cn.bing.com/?mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN&mkt=zh-CN"
headers = {'User-Agent': UserAgent().chrome}
resp = requests.get(url)
resp.encoding = 'utf-8'
info = resp.text
e = etree.HTML(info)
url = [e.xpath('//*[@id="bgLink"]/@href')][0]
title = [e.xpath('//*[@id="sh_cp"]/@title')][0]

# 先对标题和url进行处理，开始第二次开始访问图片的真实url地址
title = title[0].split("(")[0].rstrip()  # 对标题进行简单的处理，并去掉空格
url = "https://cn.bing.com" + url[0]  # 拼接真实有效的地址
if not os.path.exists("./pic"):
    os.makedirs("./pic")
resp = requests.get(url, headers={'User-Agent': UserAgent().random})
with open('./pic/{}.jpg'.format(title), 'wb') as f:
    f.write(resp.content)


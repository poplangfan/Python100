"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/2/7 10:34
"""
import re
import requests
from time import sleep
from json import loads
from jsonpath import jsonpath
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().chrome}
url = 'https://lol.qq.com/biz/hero/champion.js'
resp = requests.get(url, headers=headers)
names = re.findall(r'"\d+":"(\w+)"', resp.text)  # 获取所有的英雄名
base_url = 'https://lol.qq.com/biz/hero/{}.js'

for name in names:
    resp = requests.get(base_url.format(name), headers=headers)  # 访问所有的英雄详情页
    info = '{' + re.findall(r'("skins":.+),"info"', resp.text)[0] + '}'
    obj = loads(info)
    ids = jsonpath(obj, '$..id')
    names_ = jsonpath(obj, '$..name')
    pic_url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'  # 拼出每一个皮肤的资源路径
    for id_, name_ in zip(ids, names_):
        if '/' in name_:
            name_ = name_.replace('/', '_')  # 图片名字里有 / 需替换，否则路径出错
        with open('./hero/{}{}.jpg'.format(name, name_), 'wb') as f:
            resp = requests.get(pic_url.format(id_), headers=headers)  # 访问每一个皮肤的图片
            f.write(resp.content)
            sleep(0.5)  # 休眠
        print("正在获取{}的皮肤".format(name))
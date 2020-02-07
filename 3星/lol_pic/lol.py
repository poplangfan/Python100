"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/2/7 10:34
"""
import re
import json
import requests
from time import sleep
from json import loads
from jsonpath import jsonpath
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().chrome}


def get_alias():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    resp = requests.get(url, headers=headers)
    obj = json.loads(resp.text)
    alias = jsonpath(obj, '$..alias')
    heroIds = jsonpath(obj, '$..heroId')
    return alias, heroIds


def get_pic():
    alias, heroIds = get_alias()
    print(alias)
    for alia, heroId in zip(alias, heroIds):
        url = 'https://lol.qq.com/biz/hero/{}.js'.format(alia)
        # 第二种方法
        # url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(heroId)
        resp = requests.get(url, headers=headers)
        info = '{' + re.findall(r'("skins":.+),"info"', resp.text)[0] + '}'
        obj = loads(info)
        ids = jsonpath(obj, '$..id')
        names = jsonpath(obj, '$..name')
        pic_url = 'https://game.gtimg.cn/images/lol/act/img/skin/big{}.jpg'  # 拼出每一个皮肤的资源路径`
        # print(names)
        for id_, name in zip(ids, names):
            if '/' in name:
                name_ = name.replace('/', '_')  # 图片名字里有 / 需替换，否则路径出错
            else:
                name_ = name
            with open('./hero/{}{}.jpg'.format(alia, name_), 'wb') as f:
                print(pic_url.format(id_))
                resp = requests.get(pic_url.format(id_), headers=headers)  # 访问每一个皮肤的图片
                f.write(resp.content)
                sleep(1)  # 休眠
                print("正在获取{}_{}的皮肤".format(alia, name_))


if __name__ == '__main__':
    get_pic()

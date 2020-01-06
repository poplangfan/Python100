"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2020/1/5 21:17
"""
import re
import time
import requests
import json
from jsonpath import jsonpath

requests.packages.urllib3.disable_warnings()  # 此处关闭一个警告，去掉也无影响
cookie = "你的cookie"
UA = "你的User-Agent"
headers = {  # 这些信息都可以在Fiddler上获取
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'User-Agent': UA,
    'X-Tt-Token': 'xx',
    'x-tt-trace-id': 'xx',
    # 'Accept-Encoding': 'gzip, deflate, br',此处去掉，不然返回的数据乱码
    'X-Gorgon': 'xx',
    'X-Khronos': '1xx',
    'x-common-params-v2': 'xx',
}


def get_movie_list():
    # 抓取到的一个链接，一个链接里有十个视频
    url = "http://api3-normal-c-lq.amemv.com/aweme/v1/aweme/post/?source=0&max_cursor=1572668155000&sec_user_id=MS4wLjABAAAAElqvSzZgxtXS7vPPcAwSGzhEHuW_Jah8LBoPYDkcnYQ&count=10&ts=1578234402&_rticket=1578234399183&mcc_mnc=46007&"
    resp = requests.get(url, headers=headers, verify=False)
    obj = json.loads(resp.text)
    urls = jsonpath(obj, '$..share_info.share_url')  # 通过jsonpath获取视频的访问路径
    true_url_list = []
    for url in urls:
        if len(url) > 5:
            resp = requests.get(url, headers=headers)
            true_url = re.findall(r'playAddr: "(.+)",', resp.text)  # 通过正则获取真实URL地址
            print(true_url)
            if len(true_url) > 0:
                true_url_list.append(true_url)
    return true_url_list


def get_movie(url_list):
    cnt = 1
    for url in url_list:
        resp = requests.get(url[0], headers=headers)
        with open('./tik_movie/{}.mp4'.format(cnt), 'wb') as f:
            f.write(resp.content)
        time.sleep(2)
        print("正在获取第{}个视频".format(cnt))
        cnt += 1


if __name__ == '__main__':
    true_url_list_ = get_movie_list()
    print(true_url_list_)
    get_movie(true_url_list_)

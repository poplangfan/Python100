# -*- coding: utf-8 -*-
import time
import requests
import json
from jsonpath import jsonpath
from fake_useragent import UserAgent

#  ins上有反爬，通过分析xhr得到需要访问的真正链接，12张照片一组，通过不断地递归拿到所有照片
CNT = 0  # 计数
cookie = '你的cookie'  # 填写你自己的cookie
url_ = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&' \
           'variables=%7B%22id%22%3A%22528817151%22%2C%22first%22%3A12%2C%22after%22%3A%22{}%3D%3D%22%7D'  # 以nasa为例
base_url = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&' \
           'variables=%7B%22id%22%3A%22528817151%22%2C%22first%22%3A12%2C%22after%22%3A%22' \
           'QVFDemduRmloeXBuVTdlaDZNRjcwMVptNm9MSjFQSkZjamEyM0lVYVd4V1Z3Sk1DV3hwTFhtbzN3cFh5REd4cjBzd1JKM1dtMWxJcjFHVUFqN2JzdHpudA%3D%3D%22%7D'


def get_img(base_url_):  # 需要注意的是，抓取的图片是从13张开始，因为前12张在最初的网页
    resp = requests.get(base_url_, headers={'User-Agent': UserAgent().random, 'Cookie': cookie})  # 这里需要随机ua,否则会报错，下同
    obj = json.loads(resp.text)
    urls = jsonpath(obj, '$..display_url')
    for url_img in urls:
        global CNT
        CNT += 1
        try:
            name = url_img.split('/')[5]  # 给图片命名
            resp = requests.get(url_img, headers={'User-Agent': UserAgent().random, 'Cookie': cookie})
            with open('../ins_img/{}.jpg'.format(name), 'wb') as f:
                f.write(resp.content)
                print('正在保存第{}张图片'.format(CNT))
                time.sleep(1)
        except:
            print('第{}张图片保存失败'.format(CNT))
            continue
    judeg = jsonpath(obj, '$.data.user.edge_owner_to_timeline_media.page_info.has_next_page')[0]  # 判断是否有下一页
    if judeg:
        next_page = jsonpath(obj, '$.data.user.edge_owner_to_timeline_media.page_info.end_cursor')[0]
        if '==' in next_page:
            next_page_new = next_page.split('=')[0]
            new_page = url_.format(next_page_new)
            with open('page.txt', 'a', encoding='utf-8') as f:  # 提取每次访问的url,防止意外中断不用从头开始
                f.write(new_page + '\n')
            get_img(new_page)


get_img(base_url)

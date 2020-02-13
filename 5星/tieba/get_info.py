"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/2/11 22:09
"""
import requests
import pymongo
from lxml import etree
from collections import deque
from time import sleep
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().chrome}
# 启动Mongodb,和python交互
client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
news = client.news
new = news['new']  # 标题内容集合
url_past = news['url']  # 记录过的url集合
cnt = 0
while True:
    url = 'https://weixin.sogou.com/pcindex/pc/pc_0/3.html'
    resp = requests.get(url, headers=headers)
    print(resp.encoding)  # 网页编码方式
    info = resp.text.encode('ISO-8859-1').decode('utf-8')
    # print(info)
    e = etree.HTML(info)
    # 获取内容
    authors = e.xpath('//div[@class="s-p"]/a/text()')
    titles = e.xpath('//h3/a/text()')
    contents = e.xpath('//p/text()')
    urls = e.xpath('//h3/a/@href')
    print(authors)
    if len(authors) == len(titles) == len(contents) == len(urls):
        for author, title, content, url in zip(authors, titles, contents, urls):
            # print(new.find_one({'url': url}))
            args = {'cnt': cnt, 'author': author, 'title': title, 'content': content, 'url': url}
            if new.find_one({'url': url}):
                print('此条内容已记录')
                continue
            new.insert_one(args)
            cnt += 1
            # sleep(1)
    else:
        print('获取内容格式有误')
    sleep(3)

# url = 'https://weixin.sogou.com/'
# unvisited = deque()  # 待爬取连接集合
# visited = set()  # 已访问连接集合
# unvisited.append(url)
# headers = {'User-Agent': UserAgent().chrome}
# # 启动Mongo,和python交互
# client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
# news = client.news
# new = news['new']  # 标题内容集合
# url_past = news['url']  # 访问过的url集合
# print('开始爬取')
# cnt = 0
# cont = 0
# while unvisited:
#     # 获取链接
#     url = unvisited.popleft()
#     visited.add(url)
#     cnt += 1
#     print('开始抓取第', cnt, '页信息：', url)
#     resp = requests.get(url, headers=headers)
#     # print(resp.encoding)  # 网页编码方式
#     info = resp.text.encode('ISO-8859-1').decode('utf-8')
#     # print(info)
#     e = etree.HTML(info)
#     # for url_ in url_list:
#     #     if url_ not in unvisited and url_ not in visited:
#     #         unvisited.append(url_)
#     if url_past.find_one({'url': url}):
#         print('第{}个链接：'.format(cnt), url, '已爬取')
#         continue
#     else:
#         # 把爬取过的网页插入已访问数据库
#         args = {'id': cnt, 'url': url}
#         url_past.insert_one(args)
#         # 获取内容
#         authors = e.xpath('//div[@class="s-p"]/a/text()')
#         titles = e.xpath('//h3/a/text()')
#         contents = e.xpath('//p/text()')
#         url_lists = e.xpath('//h3/a/@href')
#         for author, title, content, url_list in zip(authors, titles, contents, url_lists):
#             if author and title and content and url_list:
#                 args = {'cnt': cnt, 'author': author, 'title': title, 'content': content, 'url': url_list}
#                 new.insert_one(args)
#                 cont += 1
#             sleep(1)
# print('爬取结束')

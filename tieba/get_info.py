# -*- coding: utf-8 -*-
import requests
import pymongo
from lxml import etree
from collections import deque
from time import sleep
from fake_useragent import UserAgent

url = 'http://shop.tata.com.cn/article_cat-5.html'
unvisited = deque()  # 待爬取连接集合
visited = set()  # 已访问连接集合
visited.add('http://shop.tata.com.cn//article_cat-15.html')
unvisited.append(url)
headers = {'User-Agent': UserAgent().chrome}
# 启动Mongo,和python交互
client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
tieba = client.tieba
tata = tieba['tata']  # 标题内容集合
url_past = tieba['url']  # 访问过的url集合
print('开始爬取')
cnt = 0
while unvisited:
    # 获取链接
    url = unvisited.popleft()
    visited.add(url)
    cnt += 1
    print('开始抓取第', cnt, '个链接：', url)
    resp = requests.get(url, headers=headers)
    info = resp.text
    e = etree.HTML(info)
    url_list = e.xpath('//div[@class="TT_list_z"]/ul/li/p/a/@href | //div[@class="list_middle list_help"]/ul/li/a/@href')
    page = e.xpath('//div[@class="TT_list_page"]/a[text()="下一页"]/@href')
    for url_ in url_list:
        x = 'http://shop.tata.com.cn/' + url_
        if x not in unvisited and x not in visited:
            unvisited.append(x)
    if page:
        page = 'http://shop.tata.com.cn/' + page[0]
        if page not in unvisited and page not in visited:
            unvisited.append(page)
    if url_past.find_one({'url': url}):
        print(cnt, '个链接：', url, '已爬取')
        continue
    else:
        # 插入数据库
        args = {'id': cnt, 'url': url}
        url_past.insert_one(args)
        # 获取内容
        type_ = e.xpath('//div[@class="TT_list"]/a/text()')
        title = e.xpath('//h1/text()')
        content = e.xpath('//div[@class="arc_nr"]/p/span/text() | //div[@class="arc_nr"]/p/span/span/text()')
        if type_ and title and content:
            args = {'cnt': cnt, 'type': type_, 'title': title, 'content': content}
            tata.insert_one(args)
        sleep(5)
print('爬取结束')


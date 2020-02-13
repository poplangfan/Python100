"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/2/11 22:09
"""
import time
import pymongo
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
url = "https://weibo.com/login"  # 微博登陆界面
driver.get(url)
driver.find_element_by_id("loginname").send_keys("xxx")
time.sleep(1)
driver.find_element_by_name("password").send_keys("xxx")
# driver.find_element(By.XPATH, '//a[text()="登录"]').click()  # 模拟点击该页面的登录，调出一个小窗口
time.sleep(20)  # 此处睡眠四十秒，确保登陆

client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
news = client.news
new = news['new']  # 标题内容表
num = news['num']  # 已访问的序号表
cnt = 0

while cnt < 21:  # 此处可以自由修改
    cnt = random.randint(1, 20)
    print(cnt)
    if num.find_one({'num': cnt}):
        print('这篇文章已经发过')
    elif not new.find_one({'cnt': cnt}):
        print('不存在这篇文章')
    else:
        args = {'num': cnt}
        num.insert_one(args)
        data = new.find_one({'cnt': cnt})
        author = data['author']
        title = data['title']
        content = data['content']
        url = data['url']
        contents_list = title + '\n' + author + '\n' + content + '\n' + '详细信息' + url
        # random.choice(contents_list)随机选择列表里的内容
        driver.find_element_by_css_selector("[title='微博输入框']").send_keys(contents_list)
        time.sleep(3)
        # 含有空格的复合类的处理方法
        driver.find_element_by_css_selector("[class='W_btn_a btn_30px ']").click()  # 点击发表
        time.sleep(3)



# driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化窗口
# url = "https://tieba.baidu.com/f?kw=%E5%92%8C%E8%87%AA%E5%B7%B1%E5%8E%BB%E6%97%85%E8%A1%8C&fr=index"  # 某一个贴吧
# driver.get(url)
# driver.find_element(By.XPATH, '//a[text()="登录"]').click()  # 模拟点击该页面的登录，调出一个小窗口
# time.sleep(10)  # 此处睡眠十秒，扫码登录百度贴吧
# # 实现自动发帖
# driver.find_element_by_name("title").clear()
# client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
# news = client.news
# new = news['new']  # 标题内容表
# num = news['num']  # 已访问的序号表
# cnt = 0
# while cnt < 21:  # 此处可以自由修改
#     cnt = random.randint(1, 20)
#     print(cnt)
#     if num.find_one({'num': cnt}):
#         print('这篇文章已经发过')
#     elif not new.find_one({'cnt': cnt}):
#         print('不存在这篇文章')
#     else:
#         args = {'num': cnt}
#         num.insert_one(args)
#         data = new.find_one({'cnt': cnt})
#         author = data['author']
#         title = data['title']
#         content = data['content']
#         url = data['url']
#         driver.find_element_by_name("title").send_keys(title)  # 此处需要预留一点空白
#         time.sleep(5)
#         driver.find_element_by_id("ueditor_replace").send_keys(author + '\n')
#         time.sleep(5)
#         driver.find_element_by_id("ueditor_replace").send_keys(content + '\n' + '详细信息：' + url)
#         time.sleep(5)
#         # 含有空格的复合类的处理方法， 此处贴吧发表会有两个不同的类名
#         try:
#             driver.find_element_by_css_selector("[class='btn_default btn_middle j_submit poster_submit']").click()
#         except:
#             driver.find_element_by_css_selector("[class='btn_middle j_submit poster_submit btn_default']").click()
#         time.sleep(random.randint(1, 3))  # 随机休眠

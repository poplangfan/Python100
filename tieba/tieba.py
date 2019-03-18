# -*- coding: utf-8 -*-
import time
import pymongo
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
url = "http://tieba.baidu.com/f?kw=tata%E6%9C%A8%E9%97%A8&fr=home"  # 某一个贴吧
driver.get(url)
driver.find_element(By.XPATH, '//a[text()="登录"]').click()  # 模拟点击该页面的登录，调出一个小窗口
time.sleep(10)  # 此处睡眠十秒，扫码登录百度贴吧
# 实现自动发帖
driver.find_element_by_name("title").clear()
client = pymongo.MongoClient()  # 有默认值，可以不写主机和端口
tieba = client.tieba
tata = tieba['tata']  # 标题内容表
num = tieba['num']  # 已访问的序号表
cnt = 50
while cnt < 101:  # 此处可以自由修改
    cnt = random.randint(1, 100)
    print(cnt)
    if num.find_one({'num': cnt}):
        print('这篇文章已经发过')
    elif not tata.find_one({'cnt': cnt}):
        print('不存在这篇文章')
    else:
        args = {'num': cnt}
        num.insert_one(args)
        data = tata.find_one({'cnt': cnt})
        type_ = data['type']
        title = data['title'][0]
        content = data['content']
        type_ = type_[0] + '-' + type_[1] + '-' + type_[2]
        driver.find_element_by_name("title").send_keys('                             ' + type_)  # 此处需要预留一点空白
        time.sleep(5)
        driver.find_element_by_id("ueditor_replace").send_keys(title + '\n')
        time.sleep(5)
        driver.find_element_by_id("ueditor_replace").send_keys(content)
        time.sleep(5)
        # 含有空格的复合类的处理方法， 此处贴吧发表会有两个不同的类名
        try:
            driver.find_element_by_css_selector("[class='btn_default btn_middle j_submit poster_submit']").click()
        except:
            driver.find_element_by_css_selector("[class='btn_middle j_submit poster_submit btn_default']").click()
        time.sleep(60 + cnt * 3)  # 随机休眠

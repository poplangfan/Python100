"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/28 0:28
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
url = "https://weibo.com/login"  # 微博登陆界面
driver.get(url)
driver.find_element_by_id("loginname").send_keys("xx")
time.sleep(1)
driver.find_element_by_name("password").send_keys("xx")
# driver.find_element(By.XPATH, '//a[text()="登录"]').click()  # 模拟点击该页面的登录，调出一个小窗口
time.sleep(40)  # 此处睡眠四十秒，确保登陆

with open("名句.txt", 'r', encoding='utf-8') as f:
    contents_list = f.read().splitlines()  # 此处直接去掉行符

cnt = 0
while True:
    # random.choice(contents_list)随机选择列表里的内容
    driver.find_element_by_css_selector("[title='微博输入框']").send_keys(random.choice(contents_list))
    time.sleep(3)
    # 含有空格的复合类的处理方法
    driver.find_element_by_css_selector("[class='W_btn_a btn_30px ']").click()  # 点击发表
    time.sleep(3)
    cnt += 1
    print("第{}次发表内容".format(cnt))
    time.sleep(601)

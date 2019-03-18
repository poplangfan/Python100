# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
url = "http://tieba.baidu.com/f?kw=tata%E6%9C%A8%E9%97%A8&fr=home"  # 某一个贴吧
driver.get(url)
driver.find_element(By.XPATH, '//a[text()="登录"]').click()  # 模拟点击该页面的登录，调出一个小窗口
time.sleep(10)  # 休眠10秒，扫码登录，一次登录，自动发帖
# 实现自动发帖，可以加个循环一直发
driver.find_element_by_name("title").clear()
# 此处有小的bug，前面必须空出一段距离，否则写的内容会被抹掉
driver.find_element_by_name("title").send_keys(" 你的标题                 你的标题")
time.sleep(1)
driver.find_element_by_id("ueditor_replace").send_keys('你想发表的内容')
time.sleep(5)
# 含有空格的复合类的处理方法
driver.find_element_by_css_selector("[class='btn_default btn_middle j_submit poster_submit']").click()  # 点击发表
time.sleep(5)


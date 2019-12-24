"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/24 22:58
"""
import sys
from you_get import common as you_get

place = "E:/PythonCode/bilibili"
url = "https://www.bilibili.com/video/av62162985"
sys.argv = ["you_get", "-o", place, url]
you_get.main()
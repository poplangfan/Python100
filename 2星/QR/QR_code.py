"""
-*- coding: utf-8 -*-
@Author  : blyang
@project : PythonCode
@Time    : 2020/3/28 21:59
"""
from MyQR import myqr

# 普通二维码
myqr.run(
    words='https://blog.csdn.net/bl_yang/article/details/105168523',
    save_name='qrcode.png'
)

# 带图片的艺术二维码：黑白
myqr.run(
    words='https://blog.csdn.net/bl_yang/article/details/105168523',
    picture='./logo.png',
    save_name='artistic.png'
)

# 带图片的艺术二维码：彩色
myqr.run(
    words='https://github.com/poplangfan/Python100',
    picture='./1.png',
    colorized=True,
    save_name='artisticColor.png'
)

# 动态二维码
myqr.run(
    words='https://blog.csdn.net/bl_yang/article/details/105168523',
    picture='./tm.gif',
    colorized=True,
    save_name='Animated.gif'
)

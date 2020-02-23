"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/29 21:24
"""
import os
import cv2

cap = cv2.VideoCapture(r'E:\ai\720P_4000K_214478702.mp4')  # 你的视频路径

images = 'E:/ai/P3/'
if not os.path.exists(images):
    os.mkdir(images)

c = 0
while True:
    success, frame = cap.read()
    if success:
        cv2.imwrite(images + str(c) + '.jpg', frame)
        c = c + 1
    else:
        break
cap.release()

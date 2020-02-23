"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/29 21:24
"""
import os
import cv2
import re

path = 'E:\\ai\\P1_out_final_3'
filelist = os.listdir(path)
# filelist_new = sorted(filelist, key=lambda i: int(re.match(r'(\d+)', i.replace('P', '')).group()))
filelist.sort(key=lambda i: int(re.match(r'(\d+)', i.replace('P', '')).group()))

# print(filelist_new)
print(filelist)
fps = 30  # 视频每秒30帧
size = (1080, 1920)  # 需要转为视频的图片的尺寸
# 可以使用cv2.resize()进行修改

video = cv2.VideoWriter("Video2.mp4", cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), fps, size)
# video = cv2.VideoWriter("VideoTest3.mp4", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)
# 视频保存在当前目录下

for item in filelist:
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + "/" + item
        print(item)
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()

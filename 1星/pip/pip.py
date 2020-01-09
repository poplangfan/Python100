# 自动化安装第三方库脚本
import os

libs = []
with open('./packages.txt', 'r', encoding='utf-8') as f:
    cont = f.read()
    conts = cont.split(',')
    for package in conts:
        libs.append(package)
print(libs)
try:
    for lib in libs:
        os.system('pip3 install ' + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple/")
    print('Successful')
except:
    print('Failed Somehow')

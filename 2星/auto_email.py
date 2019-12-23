"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/11/23 22:38
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方SMTP服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xx@qq.com"  # 你的用户名
mail_pass = "xx"  # 你生成的口令

# 设置发送人和收件人
sender = "xx@foxmail.com"  # 会显示由这个邮箱代发
receivers = "xx@qq.com"  # 你要发送给的人，目前是固定的，后面教程会读取列表

for i in range(10):
    # 发送邮件
    subject = '近来寒暑不易，希自珍慰。'  # 邮件title
    # 第一个参数为邮件内容，第二个参数为设置文本格式，第三个参数为编码设置
    message = MIMEText('万望保暖，注意御寒。', 'plain', 'utf-8')
    message['From'] = Header("blyang", 'utf-8')  # 发件人
    message['Subject'] = Header(subject, 'utf-8')  # 标题

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # qq邮箱带SSL
        smtpObj.login(mail_user, mail_pass)  # 登陆
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

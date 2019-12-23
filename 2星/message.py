"""
-*- coding: utf-8 -*-
@Author  : blyang
@Time    : 2019/12/15 21:56
"""
import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xx"
# Your Auth Token from twilio.com/console
auth_token = "xx"

client = Client(account_sid, auth_token)

send_list = ["苟利国家生死以，岂因祸福避趋之？",
             "白云一片去悠悠，青枫浦上不胜愁。",
             "醉后不知天在水，满船清梦压星河。",
             "桃李春风一杯酒，江湖夜雨十年灯。",
             "溪云初起日沉阁，山雨欲来风满楼。"]

for i in range(5):
    message = client.messages.create(
        to="+86xx",  # 收件手机号
        from_="+1 865 685 5345",
        body="{}".format(send_list[i]))
    time.sleep(1.5)
    print(message.sid)


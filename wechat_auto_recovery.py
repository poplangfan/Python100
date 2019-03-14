# -*- coding: utf-8 -*-
import time
import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # 当消息不是自己发出的时候
    if msg['FromUserName'] is not myUserName:
        itchat.send_msg(
            u"[%s]收到好友@%s 的信息： %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                                        msg['User']['NickName'], msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]我现在不在，已收到你的消息：%s, 稍后回复你' % (msg['Text'])


if __name__ == '__main__':
    itchat.auto_login()
    myUserName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run()

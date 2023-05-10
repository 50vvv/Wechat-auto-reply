""" 
作用：自动回复微信。在前一个版本基础上多了将消息转发给文件传输助手保存的功能
作者：50v
日期：2023年 05月 09日  12:18 
"""

import time

from wxauto import *

# 引入第三方库

wx = WeChat()

# 获取当前微信客户端


def WeChat_Auto_reply(reply_message):
    msgs = wx.GetAllMessage
    # 第一次获得所有信息
    message_value = [msg[1] for msg in msgs]
    # 过滤无效信息，只留下聊天记录，形成列表
    first_message = message_value[-1]
    # 以上为第一次获取最后一条信息，存在first_message中

    time.sleep(1)
    # 休眠一段时间，准备获取下一次信息

    msgs = wx.GetAllMessage
    # 第二次获取所有信息
    message_value = [msg[1] for msg in msgs]
    # 过滤无效信息，只留下聊天记录，成列表
    second_message = message_value[-1]
    # 以上为第二次获取最后一条信息，存在second_message中，为接下来if条件判断做准备

    name = [msg[0] for msg in msgs]
    user = name[-1]

    if first_message != second_message:
        wx.ChatWith(user)
        wx.SendMsg(reply_message)
        wx.ChatWith('文件传输助手')
        wx.SendMsg(f'收到消息“{message_value[-1]}”来自“{user}”，\n已回复“{reply_message}”')
        wx.ChatWith(user)
        print('收到消息，已自动回复')
    else:
        print('以上消息已回复，等待新消息')

if __name__ == '__main__':
    reply_message = input('自动回复内容：')

    while True:
        WeChat_Auto_reply(reply_message=reply_message)
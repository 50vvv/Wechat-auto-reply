""" 
作用：wx自动回复，一对一，万能回复
使用要求：必须保证微信窗口开启，不能在后台，只能对单一聊天框自动回复，使用过程中不能关闭窗口，不能切换聊天框，sleep值可依需求更改，回复信息可自改
作者：50v
日期：2023年 05月 09日  12:28 
"""

import time

from wxauto import *

# 引入第三方库

wx = WeChat()
# 获取当前微信客户端

reply_message = '你好'
# 设置回复的信息
while True:
    msgs1 = wx.GetAllMessage
    # 第一次获得所有信息
    message_value1 = [msg[1] for msg in msgs1]
    # 过滤无效信息，只留下聊天记录，形成列表
    firstmessage = message_value1[-1]
    # 以上为第一次获取最后一条信息，存在firstmessage中

    time.sleep(1)
    # 休眠一段时间，准备获取下一次信息

    msgs2 = wx.GetAllMessage
    # 第二次获取所有信息
    message_value2 = [msg[1] for msg in msgs2]
    # 过滤无效信息，只留下聊天记录，成列表
    secondmessage = message_value2[-1]
    # 以上为第二次获取最后一条信息，存在secondmessage中，为接下来if条件判断做准备

    if firstmessage != secondmessage:
        print('有新消息！已回复“你好”')
        wx.SendMsg(reply_message)
    else:
        print("上面已回复，不再进行自动回复，等待新的消息")

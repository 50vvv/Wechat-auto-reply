""" 
作用：
作者：50v
日期：2023年 05月 11日  17:56 
"""
import time
from def库 import *

# 引入第三方库

wx = WeChat()

other_list = ['订阅号']


# 获取当前微信客户端

def WeChat_Auto_reply():
    # while True:

    first_user = Get_Dynamic_Contacts()  # 获取第一时刻列表顶部联系人
    time.sleep(3)  # 歇一秒
    second_user = Get_Dynamic_Contacts()  # 获取第二时刻列表顶部联系人
    list_second_user = second_user.split()  # 转为set形式，方便比较包含关系

    if first_user != second_user:  # 判断是否有新的顶部联系人
        if not set(list_second_user).issubset(set(other_list)):  # 如果不在特殊名单中，自动回复
            wx.ChatWith(second_user)  # 转到新顶部联系人聊天框
            accept_message = Get_New_Message()  # 获取新顶部联系人发来的最后一条消息
            thisuser = Get_Last_Name()  # 获取该窗口最后一条消息来源人昵称
            reply_message = f'[自动回复]你好“{thisuser}”，我现在不在！'
            wx.SendMsg(reply_message)  # 发送自动回复内容
            wx.ChatWith('文件传输助手')  # 转到文件传输助手聊天框
            wx.SendMsg(f'收到消息“{accept_message}”来自“{thisuser}”，\n已回复“{reply_message}”')  # 将相关信息发送，方便查阅
            wx.ChatWith(thisuser)  # 回到刚才的聊天框
            print('第一if判断：收到消息，已自动回复')  # 命令行输出
        else:
            print('第一if判断：以上消息已回复，等待新消息')  # 在特殊名单内，不自动回复，命令行输出
    else:
        print('第一if判断：以上消息已回复，等待新消息')  # 没有新的顶部联系人，不自动回复，命令行输出

    first_message = Get_New_Message()  # 获取第一时刻最后一条消息
    # print(first_message)
    time.sleep(3)  # 休息一秒
    second_message = Get_New_Message()  # 获取第二时刻最后一条信息
    user = Get_Last_Name()  # 获取该窗口最后一条消息来源人昵称

    if first_message != second_message:  # 该聊天框是否产生新消息，如果产生，自动回复
        wx.ChatWith(user)  # 转到该聊天框（无用
        reply_message = f'[自动回复]你好“{user}”，我现在不在！'
        wx.SendMsg(reply_message)  # 自动回复
        wx.ChatWith('文件传输助手')  # 转到文件传输助手
        wx.SendMsg(f'收到消息“{second_message}”来自“{user}”，\n已回复“{reply_message}”')  # 发送有关信息
        wx.ChatWith(user)  # 回到刚才聊天框
        print('第二if判断：收到消息，已自动回复')  # 命令行输出
    else:
        print('第二if判断：以上消息已回复，等待新消息')  # 如果没有，则不自动回复，命令行输出


if __name__ == '__main__':
    while True:
        WeChat_Auto_reply()

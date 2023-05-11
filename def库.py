from wxauto import *

wx = WeChat()


def Get_Dynamic_Contacts():
    user_list = wx.GetSessionList()
    first_user = user_list[0]
    return first_user

def Get_New_Message():
    msgs = wx.GetAllMessage
    # 第一次获得所有信息
    message_value = [msg[1] for msg in msgs]
    # 过滤无效信息，只留下聊天记录，形成列表
    first_message = message_value[-1]
    return first_message
    # 以上为第一次获取最后一条信息，存在first_message中

def Get_Last_Name():
    msgs = wx.GetAllMessage

    name = [msg[0] for msg in msgs]
    user = name[-1]
    return user


if __name__ == '__main__':
    print(Get_Dynamic_Contacts())

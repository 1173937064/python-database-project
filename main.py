from tkinter import *
from LoginPage import *

if __name__=='__main__':    
    window = Tk()
    window.title('星动APP')
    LoginPage(window)
#    input()


#可以创建用户，以及用户更改信息，并用hash给密码这些信息加密
#可以尝试给用户_用户权限，并完善日志功能
#用tmp创表，记录每个用户浏览网页记录，关闭数据库就关闭了该表
#管理员账号密码：admin
#增加图片得定义要在__init__进行
#试着爬B站运动区弹幕

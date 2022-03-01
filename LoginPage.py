from tkinter import *
from tkinter.messagebox import *        #showinfo 函数
from pymysql import *
from MainPage import *
from Admin import *
from Register import *
import sqlite3
#登录界面
class LoginPage(object):
    def __init__(self, control=None):
        self.root = control            
        self.root.geometry('%dx%d' % (800, 500))        #设置窗口大小
        #连接db文件
        try:
            self.conn=sqlite3.connect("test.db")
        except:
            print("失败")
        
        #连接本地数据库
        #self.conn=connect(host='localhost',user='root',passwd='xiaohongbo',db='sms',charset='utf8')
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
        
    def createPage(self):
            self.page = Frame(self.root) #创建Frame
            self.page.pack()
            Label(self.page).grid(row=0, stick=W)
            Label(self.page).grid(row=1, stick=W)
            Label(self.page, text = '欢迎使用星动APP', fg='red',font=('宋体',11)).grid(row=2,column=1)
            Label(self.page).grid(row=3, stick=W)
            Label(self.page).grid(row=4, stick=W)
            Label(self.page).grid(row=5, stick=W)
            Label(self.page, text = '账号: ',fg='green').grid(row=6, stick=W, pady=10)
            Entry(self.page, textvariable=self.username).grid(row=6, column=1, stick=E)
            Label(self.page, text = '密码: ', fg='green').grid(row=7, stick=W, pady=10)
            Entry(self.page, textvariable=self.password, show='*').grid(row=7, column=1, stick=E)
            Button(self.page, text='登陆', command=self.loginCheck, fg='blue').grid(row=8, stick=W, pady=10)
            Button(self.page,text='管理员登录',command=self.adminLogin,fg='blue').grid(row=10,column=1,stick=E)
            Button(self.page,text='用户注册',command=self.userRegister,fg='blue').grid(row=10,column=0,stick=E)
            Button(self.page, text='退出', command=self.pageQuit, fg='blue').grid(row=8, column=1, stick=E)
            


    def loginCheck(self):
            name = self.username.get()
            secret = self.password.get()
            cursor = self.conn.cursor()
            sql = "select pno,pwd from consumer"
            cursor.execute(sql)
            Pass = cursor.fetchall()
            try:
                for na in Pass:
                    if int(name) == int(na[0]):
                        if int(secret) == int(na[1]):
                            sql =  ''' CREATE TEMPORARY TABLE tmp ( 
      history VARCHAR(30),
      user VARCHAR(30),
      time_add VARCHAR(50) );
      '''

                            cursor.execute(sql)
                            sql = 'select name from consumer where pno='+name
                            cursor.execute(sql)
                            name1 = cursor.fetchone()
                            name2 = name1[0]
                            sql = 'insert into tmp(user) values(\''+name2+'\')'
                            cursor.execute(sql)
                            self.conn.commit()
                            self.page.destroy()
                            MainPage(self.root,self.conn)
            except:
                showinfo(title='错误', message='账号或密码错误！(something mistake)')
                
    def pageQuit(self):
        self.root.destroy()

    def adminLogin(self):
       # self.root.destroy()
       # Adminlogin(self.conn)
        if self.username.get() == 'admin' and self.password.get() == 'admin':
            self.root.destroy()
            Adminlogin(self.conn)
        else:
            showinfo(title='错误',message='管理员账号或密码错误')
    def userRegister(self):
        self.root.destroy()
        UserRegister(self.conn)

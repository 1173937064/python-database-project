from easygui import *
from sys import exit
class UserRegister(object):
    def __init__(self,conn):
        self.conn = conn
        self.Message_user()
    def Message_user(self):
        while True:
            Message = multenterbox(msg='用户注册界面',title='星动APP',fields=['姓名','账号','性别','密码'])
            sql = 'select * from consumer'
            cursor = self.conn.cursor()
            cursor.execute(sql)
            pno = cursor.fetchall()
            for i in pno:
                if Message[1]==str(i[1]):
                    choice = ccbox(msg='账号已存在',title='错误',choices=('返回注册界面','退出'))
                    if choice == True:
                        break
                    else:
                        self.conn.close()
                        exit()
                else :
                    x=['男','女']
                    if Message[2] not in x:
                        choice = ccbox(msg='性别输入错误',title='错误',choices=('返回注册界面','退出'))
                        if choice == True:
                            break
                        else:
                            self.conn.close()
                            exit()
                    else:
                        sql = 'insert into consumer(name,pno,sex,pwd) values( '+'\''+Message[0]+'\','+str(Message[1])\
                          +',\''+Message[2]+'\',\''+Message[3]+'\');'
                        cursor.execute(sql)
                        msgbox(msg='创建成功！重新登录程序即可登录！',title='成功',ok_button='确定')
                        self.conn.close()
                        exit()
                        
                    
                
                    
                    
        
        

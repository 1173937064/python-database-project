from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from ViewPage import *

#主界面
class MainPage(object):
    def __init__(self, control, conn):
            self.root = control         #定义内部变量root，将LoginPage的窗口数据传过来
            self.root.geometry('%dx%d' % (800, 830)) #设置窗口大小
            self.conn = conn
            self.createPage()

    def createPage(self):
            #页面创建
            self.homePage = HomeFrame(self.root,self.conn)
            self.meatPage = MeatFrame(self.root,self.conn)
            self.lifePage = LifeFrame(self.root,self.conn)
            self.snacksPage = SnacksFrame(self.root,self.conn)
            self.drinkPage = DrinkFrame(self.root,self.conn)
            self.milkPage = MilkFrame(self.root,self.conn)
            self.fruit_vegetablesPage = Fruit_vegetablesFrame(self.root,self.conn)
            self.returnPage = ReturnFrame(self.root,self.conn)
            self.accountPage = AccountFrame(self.root,self.conn)
            self.fayanjiluPage = FayanjiluFrame(self.root,self.conn)
            self.aboutPage = AboutFrame(self.root,self.conn)
            self.homePage.pack()            #默认显示数据录入界面
            menubar = Menu(self.root)
                           
            #下拉菜单
            filemenu = Menu(menubar, tearoff=0)         #tearoff意为下拉
            menubar.add_cascade(label='运动科普', menu=filemenu)
            filemenu.add_command(label='篮球' ,command= self.meatData)
            filemenu.add_command(label='足球' ,command=self.lifeData)
            filemenu.add_command(label='乒乓球', command=self.snacksData)
            filemenu.add_command(label='排球',command=self.drinkData)
            filemenu.add_command(label='100m赛跑',command=self.milkData)
            filemenu.add_command(label='跳水',command=self.fruit_vegetablesData)

            menubar.add_command(label='交友处', command = self.returnData)
            menubar.add_command(label='浏览记录', command = self.accountData)
            menubar.add_command(label='发言记录',command = self.fayanjiluData)
            menubar.add_command(label='关于',command = self.aboutData)
            menubar.add_command(label='退出', command = self.loginout)
            self.root['menu'] = menubar     # 设置菜单栏
    def homeData(self):
            self.homePage.pack()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def meatData(self):
            self.homePage.pack_forget()
            self.meatPage.pack()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def lifeData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def snacksData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()

    def drinkData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def milkData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def fruit_vegetablesData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()

#第一级菜单
    def returnData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
    def accountData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack_forget()
            
    def fayanjiluData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack()
            self.aboutPage.pack_forget()

    def aboutData(self):
            self.homePage.pack_forget()
            self.meatPage.pack_forget()
            self.lifePage.pack_forget()
            self.snacksPage.pack_forget()
            self.drinkPage.pack_forget()
            self.milkPage.pack_forget()
            self.fruit_vegetablesPage.pack_forget()
            self.returnPage.pack_forget()
            self.accountPage.pack_forget()
            self.fayanjiluPage.pack_forget()
            self.aboutPage.pack()
    def loginout(self):
            self.conn.close()
            self.root.destroy()

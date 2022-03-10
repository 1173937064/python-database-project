from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import webbrowser
#主页
class HomeFrame(Frame):     #Frame由self.root传过来值
        def __init__(self, control, conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.itemName = StringVar()
                self.home = ImageTk.PhotoImage(Image.open('./pic/yundong.jpg'))
                #self.bg = ImageTk.PhotoImage(Image.open('bg.webp'))
                self.createPage()
        def createPage(self):
                #canvas_root = Canvas(self, width=800, height=830)
                #canvas.creat_image(800,830,image=self.bg).pack()
                Label(self,text='欢迎使用星动APP').grid(column=0,row=0)
                Label(self,image=self.home).grid(column=0,row=2)

#篮球
class MeatFrame(Frame): # 继承Frame类
        def __init__(self, control, conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.lanqiu = ImageTk.PhotoImage(Image.open('./pic/lanqiu.jpeg'))
                self.createPage()

        def createPage(self):
                Label(self, text='篮球介绍',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self, text=
                      """
篮球（basketball），是奥运会核心比赛项目，是以手为中心的身体对抗
性体育运动。1891年12月21日，由美国马萨诸塞州斯普林菲尔德基督教青
年会训练学校体育教师詹姆士·奈史密斯发明。1896年，篮球运动传入中
国天津。1904年，圣路易斯奥运会上第1次进行了篮球表演赛。1936年，篮
球在柏林奥运会中被列为正式比赛项目，中国也首次派出篮球队参加奥运
会篮球项目。1992年，巴塞罗那奥运会开始，职业选手可以参加奥运会篮球
比赛。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.lanqiu).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)

        def Buy(self):
                cursor = self.conn.cursor()
                sql = "insert into tmp(history,time_add) values('篮球页',datetime('now','localtime'))"
                cursor.execute(sql)
                webbrowser.open('https://baike.baidu.com/item/%E7%AF%AE%E7%90%83/123564?fr=aladdin',new=0)
#足球
class LifeFrame(Frame):     #Frame由self.root传过来值
        def __init__(self, control,conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.zuqiu = ImageTk.PhotoImage(Image.open('./pic/zuqiu.jpg'))
                self.createPage()

        def createPage(self):
                Label(self, text='足球',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self,text=
                      """
足球（Football[英]、 Soccer[美]）是一项以脚为主，控制和支配球，两支球队按照
一定规则在同一块长方形球场上互相进行进攻、防守对抗的体育运动项目。因足球运动
对抗性强、战术多变、参与人数多等特点，故被称为“世界第一运动”。现代足球的前
身起源于中国古代山东淄州（今淄博市）的球类游戏“蹴鞠”，后经阿拉伯人由中国传
至欧洲，逐渐演变发展为现代足球。现代足球始于英国。1848年，足球运动历史上第一
部文字形式的规则《剑桥规则》诞生。1863年10月26日，英格兰成立了世界上第一所足
球协会，并统一了足球运动的竞赛规则。1872年，英格兰与苏格兰之间举行了足球史上
第一次协会间的正式比赛。1900年，在第二届夏季奥林匹克运动会中，足球被列入正式
项目。足球在全球被广泛译为“Football”,只有在美国等极少数国家被译为“Soccer”，
而“Football”在美国、加拿大被指为“美式橄榄球”。足球的最高组织机构为国际足
球联合会，成立于1904年，总部设于瑞士苏黎世。中国最高组织机构是中国足球协会，
1955年1月3日成立于北京。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.zuqiu).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)
        def Buy(self):
                cursor = self.conn.cursor()
                sql = "insert into tmp(history,time_add) values('足球页',datetime('now','localtime'))"
                cursor.execute(sql)
                webbrowser.open('https://baike.baidu.com/item/%E8%B6%B3%E7%90%83/122380?fr=aladdin',new=0)
#乒乓球
class SnacksFrame(Frame): # 继承Frame类
        def __init__(self, control,conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.pingpangqiu = ImageTk.PhotoImage(Image.open('./pic/pingpangqiu.jpg'))
                self.createPage()

        def createPage(self):
                Label(self, text='乒乓球',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self,text=
                      """
乒乓球（table tennis），被称为中国的“国球”，是一种世界流行的
球类体育项目，包括进攻、对抗和防守。乒乓球起源于英国，“乒乓球”
一名起源自1900年，因其打击时发出“Ping Pong”的声音而得名。在中
国大陆以“乒乓球”作为它的官方名称，中国香港及澳门等地区亦同。
1926年1月，在德国柏林举行了一次国际乒乓球赛，共有9个国家的64名男
运动员参加了比赛。同年12月，国际乒乓球联合会正式成立，并把在伦敦
举行的欧洲锦标赛命名为第一届世界乒乓球锦标赛。乒乓球组织机构设有
国际乒乓球联合会、亚洲乒乓球联盟、中国乒乓球协会。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.pingpangqiu).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)
        def Buy(self):
                cursor = self.conn.cursor()
                sql = "insert into tmp(history,time_add) values('乒乓球',datetime('now','localtime'))"
                cursor.execute(sql)
                webbrowser.open('https://baike.baidu.com/item/%E4%B9%92%E4%B9%93%E7%90%83/221415?fr=aladdin',new=0)
#排球
class DrinkFrame(Frame): # 继承Frame类
        def __init__(self, control,conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.paiqiu = ImageTk.PhotoImage(Image.open('./pic/paiqiu.jpg'))
                self.createPage()

        def createPage(self):
                Label(self, text='排球',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self,text=
                      """
排球（volleyball），是球类运动项目之一，球场长方形，中间隔有高网，比赛双方
（每方六人）各占球场的一方，球员用手把球从网上空打来打去。排球运动使用的球，
用羊皮或人造革做壳，橡胶做胆，大小和足球相似。排球运动源于美国，1895年，美国
马萨诸塞州霍利约克市，由韦廉姆·G·摩根发明；1900年左右，排球自美国传入加拿大。
1905年，排球传入古巴、巴西、中国等国家，成为当时风靡美洲的一项时尚运动。1949年，
首届世界男子排球锦标赛在捷克斯洛伐克的布拉格举办。排球最高级的组织机构为国际排
球联合会，截至2020年9月，共有222个协会会员，分属欧洲、亚洲、非洲、中北美和加勒
比地区、南美5个洲级排球联合会。中国排球协会是中华全国体育总会的团体会员，是中国
奥林匹克委员会承认的全国性专项运动协会。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.paiqiu).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)
        def Buy(self):
                cursor = self.conn.cursor()
                sql = "insert into tmp(history,time_add) values('排球',datetime('now','localtime'))"
                cursor.execute(sql)
                webbrowser.open('https://baike.baidu.com/item/%E6%8E%92%E7%90%83/33349?fr=aladdin',new=0)

#100m赛跑
class MilkFrame(Frame): # 继承Frame类
        def __init__(self, control,conn):
                Frame.__init__(self, control)
                self.root = control #定义内部变量root
                self.conn = conn
                self.yibaimi = ImageTk.PhotoImage(Image.open('./pic/100m.jpg'))
                self.createPage()

        def createPage(self):
                Label(self, text='100m赛跑',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self,text=
                      """
100米赛跑是一项室外田径短跑项目，同时也是最流行、最知名的田径项目之一。
该项目为短距离径赛项目，须使用起跑器起跑。在现代奥运会中，男子100米从
1896年开始成为正式比赛项目，而女子100米则是从1928年开始。获得100米奥运
冠军的人通常被称为“世界上跑的最快的人”。男子100米的世界纪录是由牙买
加运动员尤塞恩·博尔特在柏林世界田径锦标赛中跑出的9.58秒，女子世界纪录
是由美国运动员弗洛伦斯·格里菲斯-乔伊娜在美国奥运选拔赛复赛中跑出的10.49秒。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.yibaimi).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)
        def Buy(self):
                cursor = self.conn.cursor()
                sql = "insert into tmp(history,time_add) values('100m赛跑',datetime('now','localtime'))"
                cursor.execute(sql)
                webbrowser.open('https://baike.baidu.com/item/100%E7%B1%B3%E8%B5%9B%E8%B7%91/10645264?fr=aladdin',new=0)

#跳水
class Fruit_vegetablesFrame(Frame): # 继承Frame类
    def __init__(self, control,conn):
            Frame.__init__(self, control)
            self.root = control #定义内部变量root
            self.conn = conn
            self.tiaoshui = ImageTk.PhotoImage(Image.open('./pic/tiaoshui.webp'))
            self.createPage()

    def createPage(self):
                Label(self, text='跳水',font=("华文行楷",30)).grid(row=0,column =2)
                Label(self,text=
                      """
跳水（Diving）是一项优美的水上运动，它是从高处用各种姿势跃入水中或是从跳水器械
上起跳，在空中完成一定动作姿势，并以特定动作入水的运动。1900年第2届奥运会上，
瑞典人在特制的跳台上表演了各种跳水动作。跳水的历史非常久远。从人类掌握游泳技能
后，就开始有了简单的跳水活动。1904年，第3届奥运会开始设立了男子高度跳水和男子跳
台跳水两个比赛项目。1951年，跳水才成为规则完整的奥运会正式比赛项目。跳水从1951年
第一届亚运会开始，就成为正式的亚运会比赛项目。跳水运动的世界组织机构是国际业余
游泳联合会，成立于1908年，总部设在瑞士的洛桑。中国跳水机构组织是中国跳水协会，
2020年1月11日在北京宣布成立。
                      """,font=("宋体")).grid(row=1,column=2)
                Label(self,image=self.tiaoshui).grid(row=2,column=2)
                Button(self, text='了解更多',command=self.Buy).grid(row=3, column=2)
    def Buy(self):
            cursor = self.conn.cursor()
            sql = "insert into tmp(history,time_add) values('跳水',datetime('now','localtime'))"
            cursor.execute(sql)
            webbrowser.open('https://baike.baidu.com/item/%E8%B7%B3%E6%B0%B4/708?fr=aladdin',new=0)
#交友处
class ReturnFrame(Frame): # 继承Frame类
    def __init__(self, control, conn):  #成功传入数据库
            Frame.__init__(self, control)
            self.root = control #定义内部变量root
            self.cmd = StringVar()
            self.conn = conn
            self.jiaoyou = ImageTk.PhotoImage(Image.open('./pic/jiaoyou.jpg'))
            self.createPage()
            
    def createPage(self):
            
            Label(self,text='差不多完成').grid(row=0, column=2)
            Label(self,image=self.jiaoyou).grid(row=1,column=2)
            Entry(self, textvariable=self.cmd).grid(row=2, column=2, ipadx=10,ipady=10)
            Button(self, text='发言',command=self.executeCmd).grid(row=2, column=3)
            self.refresh_data()
  
    def refresh_data(self):                                     #完成实时刷新数据（after()）
            cursor = self.conn.cursor()
            sql = 'select * from jiaoyou'
            cursor.execute(sql)
            name = cursor.fetchall()        
            t=4
            for i in name:
                Label(self,text=i).grid(row=t,column=2)
                t = t+1
            self.after(5000,self.refresh_data)
    def executeCmd(self):
            cursor = self.conn.cursor()
            #查询账号
            sql = 'select user from tmp'
            cursor.execute(sql)
            jieguo = cursor.fetchone()
            pno = jieguo[0]
            sql = 'insert into jiaoyou(fayan,time,pno) values('+'\''+self.cmd.get()+'\''+",datetime('now','localtime'),\'"+pno+'\')'
            cursor.execute(sql)
            self.conn.commit()

#发言记录
class FayanjiluFrame(Frame): # 继承Frame类
    def __init__(self, control,conn):
            Frame.__init__(self, control)
            self.root = control #定义内部变量root
            self.conn = conn
            self.enter = StringVar()
            self.history = None
            self.createPage()

    def createPage(self):
            Label(self,text="历史发言").grid(row=0, column=1)
            Label(self,text='输入要删除的发言序号：').grid(row=1,column=1)
            Entry(self, textvariable=self.enter).grid(row=2, column=1)
            Button(self, text='删除',command= lambda:self.executeCmd(self.history)).grid(row=2, column=2)
            self.refresh_data()
            
    def refresh_data(self):
            cursor = self.conn.cursor()
            sql = 'select user from tmp'
            cursor.execute(sql)
            name1 = cursor.fetchone()
            name2 = name1[0]
            sql = "select * from jiaoyou where pno='"+name2+'\''
            cursor.execute(sql)
            history = cursor.fetchall()
            t=3
            self.history = history
            history1 = list(history)
            for i in history1:
                a = str(t-2)+'.内容:'+i[0]+'\t'+i[1]+'   用户名:'+i[2]
                Label(self,text=a).grid(row=t,column=1)
                t = t+1
            self.after(5000,self.refresh_data)
    def executeCmd(self,history):
            cursor = self.conn.cursor()
            try:
                    time_tmp = history[int(self.enter.get())-1][1]
                    sql = 'delete from jiaoyou where time=\''+str(time_tmp)+'\''
                    cursor.execute(sql)
                    self.conn.commit()
            except:
                    showinfo(title='错误',message='检查输入！')

            else:
                    showinfo(title='提醒',message='删除成功！')



#浏览记录
class AccountFrame(Frame): # 继承Frame类
    def __init__(self, control,conn):
            Frame.__init__(self, control)
            self.root = control #定义内部变量root
            self.conn = conn
            self.createPage()

    def createPage(self):
            cursor = self.conn.cursor()
            Label(self, text='查询界面').grid(row=0,column=1)
            Button(self, text='浏览记录查询',command=self.Makesure).grid(row=10, column=10)
           
    def Makesure(self):
            cursor = self.conn.cursor()
            Label(self, text='记录').grid(row=1,column=1)
            sql = 'select history,time_add from tmp '
            cursor.execute(sql)
            name = cursor.fetchall()        
            t=2
            for i in name:
                Label(self,text=i).grid(row=t,column=1)
                t = t+1

#关于
class AboutFrame(Frame): # 继承Frame类
    def __init__(self, control,conn):
            Frame.__init__(self, control)
            self.root = control #定义内部变量root
            self.conn = conn
            self.createPage()

    def createPage(self):
            cursor = self.conn.cursor()
            #frame1 = Frame(self.root, relief=RAISED, borderwidth=2)
            #Label(self, text='关于界面').pack()
            Label(self).grid(row=0, stick=W, pady=10)
            self.text="""
若遇到问题请联系管理员
QQ：1234567789
邮箱：guanliyuan@gmail.com
"""
            Label(self,text=self.text).grid(row=0, column=0, stick= E)

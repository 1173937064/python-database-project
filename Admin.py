from easygui import *
from sys import exit
class Adminlogin(object):
    def __init__(self,conn):
        while True:
            self.conn = conn
            choice = buttonbox(msg='星动APP后台',title='主页',choices=('商品情况','消费者信息','日志','员工情况(暂未完成)','退出'))
            if choice == '商品情况':
                self.Goods()
            elif choice == '消费者信息':
                self.Consumer()
            elif choice == '日志':
                self.Log()
            elif choice == '员工情况(暂未完成)':
                self.Staff()
            else :
                self.Out()


    def Goods(self):
        cursor = self.conn.cursor()
        sql = ''
        choice = buttonbox(msg='查询信息',title='商品页',choices=('果蔬','奶制品','肉制品','饮品','零食','日用品','返回上一层'))
        if choice == '果蔬':
            self.Guoshu()
        elif choice == '奶制品':
            self.Naizhipin()
        elif choice == '肉制品':
            self.Rouzhipin()
        elif choice == '饮品':
            self.Yinpin()
        elif choice == '零食':
            self.Lingshi()
        elif choice == '日用品':
            self.Riyongpin()
        else :
            return
        
    def Guoshu(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'果蔬\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='果蔬页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':    
            list1 = multenterbox(msg='增加果蔬',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'果蔬\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='删除果蔬',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return
        
    def Naizhipin(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'奶制品\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='奶制品页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':
            list1 = multenterbox(msg='增加新品种',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'奶制品\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='删除奶制品',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return

    def Rouzhipin(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'肉制品\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='肉制品页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':
            list1 = multenterbox(msg='增加新品种',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'肉制品\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='删除肉制品',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return


    def Yinpin(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'饮品\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='饮品页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':
            list1 = multenterbox(msg='增加新品种',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'饮品\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='删除饮品',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return

    def Lingshi(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'零食\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='零食页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':
            list1 = multenterbox(msg='增加新品种',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'零食\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='删除零食',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return

    def Riyongpin(self):
        cursor = self.conn.cursor()
        sql = "select * from goods where type=\'日用品\'"
        cursor.execute(sql)
        all = cursor.fetchall()
        choice1 = buttonbox(msg=all,title='日用品页',choices=('增加','删除','更新','返回主页'))
        if choice1 == '增加':
            list1 = multenterbox(msg='增加新品种',title = '增加页',fields=['商品号','名字','价格','数量'])
            sql = "insert into goods values(" +'\''+list1[0]+'\','+'\''+list1[1]+'\','+'\''+str(list1[2])+'\','+'\''+str(list1[3])+'\',\'日用品\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='增加失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='增加成功',title='成功',ok_button='确认')
        elif choice1 == '删除':
            list1 = multenterbox(msg='日用品删除',title = '删除页',fields=['名字'])
            sql = "delete from goods where(" +'name='+'\''+list1[0]+ '\')'
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='删除失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='删除成功',title='成功',ok_button='确认')
        elif choice1 == '更新':
            list1 = multenterbox(msg='更新价格和数量',title = '更新页',fields=['名字','价格','数量'])
            sql = "update goods set " +'price=\''+list1[1]+'\','+'number=\''+list1[2]+'\' '+'where(name='+'\''+list1[0]+'\')'
            print(sql)
            try:
                cursor.execute(sql)
            except:
                msgbox(msg='更新失败',title='错误',ok_button='确认')
            else:
                msgbox(msg='更新成功',title='成功',ok_button='确认')
        else:
            return
    def Consumer(self):
        cursor = self.conn.cursor()
        sql = 'select * from consumer'
        cursor.execute(sql)
        name = cursor.fetchall()
        msgbox(msg=name,title='消费者信息',ok_button='确认')
    def Log(self):
        cursor = self.conn.cursor()
        sql = 'select * from goods_log'
        cursor.execute(sql)
        name = cursor.fetchall()
        out = ccbox(msg=name,title='日志文件',choices=('删除所有消费者日志文件','退出'))
        if out == '删除所有消费者日志文件':
            sql = 'delete from goods_log where action=\'消费者购买\''
            cursor.execute(sql)
            msgbox(msg='成功',title='成功',ok_button='确认')
    def Staff(self):
        pass
    def Out(self):
        self.conn.close()
        exit()

# coding:utf8  #别忘了设置python编码
import sys
import MySQLdb
 
class TransferMoney(object):
    def __init__(self,con):
        self.con=con
    
    def check_account(self, transfers):
        cursor=self.con.cursor()
        try:
            sql="select * from user where _id=%s" % transfers
            print '查询语句:'+sql
            cursor.execute(sql)
            rs=cursor.fetchall();#从结果中取出多有记录
            if len(rs)!=1:
                raise Exception("查无此人")
        finally:
            cursor.close();
        
    def has_enough_momey(self,transfers, money):
        cursor=self.con.cursor()
        try:
            sql="select _money from user where _id=%s and _money>%s" % (transfers,money)
            print '余额语句:'+sql
            cursor.execute(sql)
            rs=cursor.fetchall();
            if len(rs)!=1:
                raise Exception("余额不足")
        finally:
            cursor.close();
    
    def reduce_money(self,transfers,money):
        cursor=self.con.cursor()
        try:
            sql="update user set  _money=_money-%s where _id=%s" % (money,transfers)
            print '转账语句:'+sql
            cursor.execute(sql)
            rs=cursor.rowcount;
            if rs!=1:
                raise Exception("转账失败")
        finally:
            cursor.close();
    
    def add_money(self, receives, money):
        cursor=self.con.cursor()
        try:
            sql="update user set  _money=_money+%s where _id=%s" % (money,receives)#这里多个参数需要加括号
            print '转账语句:'+sql
            cursor.execute(sql)
            rs=cursor.rowcount;#这里需要使用rowcount获取被改变的行数，而不是fetch结果集
            if rs!=1:
                raise Exception("加钱失败")
        finally:
            cursor.close();
    
    def transfer(self,transfers,receives,money):
        try:
            self.check_account(transfers)
            self.check_account(receives)
            self.has_enough_momey(transfers,money)
            self.reduce_money(transfers,money)
            self.add_money(receives,money)
            self.con.commit()
        except Exception as e:
            raise e
            self.con.rollback()
    def showmoneyT(self,transfers):
        cursor=self.con.cursor()
        try:
            sql="select _money from user where _id=%s" % (transfers)
            cursor.execute(sql)
            rs=cursor.fetchall();#fetch结果集
            for i in range(len(rs)):
                print "转账人现有存款：",rs[i]
        finally:
            cursor.close(); 
    def insertuser(self,myid,money):
        cursor = self.con.cursor()
        try:
            sql = "insert into user(_id,_money) values(%s,%s)" %(myid,money)
            cursor.execute(sql)
            #rs=cursor.rowcount();#这里需要使用rowcount获取被改变的行数，而不是fetch结果集
        finally:
            cursor.close()
if __name__=='__main__':
    transfers = '0001'
    receivsys = '0002'
    print "进行插入功能测试："
    myid = str(raw_input('请输入要添加的用户id:\n')) 
    money = raw_input('请输入要添加的用户金额:\n')
    #con = MySQLdb.connect(host='localhost',user='root',passwd='flydog',db='test',charset='utf8')
    con=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='flydog',db='test',charset='utf8')
    tr_money=TransferMoney(con) 
    tr_money.insertuser(myid,money)
    tr_money.showmoneyT(transfers)
    money = raw_input("请输入转账的金额！")
    try :
        print "----------------------------------------------"
        print "----------------经过下列流程-------------------"
        tr_money.transfer(transfers,receivsys,money)
        print "----------------------------------------------"
        print "----------------------------------------------"
        print "经过成功转账："
        tr_money.showmoneyT(transfers)
    except Exception as e:
        print '转账出错：'+str(e)
    finally:
        con.close()
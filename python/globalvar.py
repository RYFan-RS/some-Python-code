#_*_ coding: utf-8 _*_
Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
   str= input("please input something:"+/next)#.encode('utf-8')
   print str,"is your input"#.encode('utf-8')
 
print Money
AddMoney()
print Money
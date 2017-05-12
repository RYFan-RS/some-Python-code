import random
num = random.randrange(1,200,2)
print num
num2 = raw_input("请输入一个数字")
if(num2.isdigit()):
    print num*int(num2)
else:
    print "你输入的不是数字"
"""
try:
    num = 1/0
#except:
    #print "分母不能为0"
except ZeroDivisionError:
    print "分母不能为0"
    print ZeroDivisionError
else:
    print "运行正常！"
try:
    num3 = 1/1
finally:
    print "in finally now"
"""
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print "raise出分母不能为0"
username = "admin"
password = "admin"
assert username = "admin" and password = "NOTadmin",'密码错误'
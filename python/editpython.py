# _*_ coding:utf-8 _*_
import random
print 'ok in editplus'
def num(a,b):
	print a+b
	return
num(9,10)
def printnum():
	num=random.randrange(2,2000)
	print num
printnum()
def a(x):
    """
    闭包
    """
    def b(y):
        return x+y
    return b
print a(2)(3)
def swap(x,y):
    print (u"交换之前".encode('utf-8'))
    print ('x=',x,'y=',y)
    x,y = y,x
    print (u"交换之后".encode('utf-8'))
    print ('x=',x,'y=',y)   
swap(1,2)
d_num = [0,6]
d_num[1:1] = [1,2,3,4,5]
print d_num
list_sort = [1,2,4,3,0,9,7,8,6]
print list_sort.sort()
print list_sort.index(9)
print "反向输出：",list_sort.reverse()#reverse()和sort()一样只改变列表但不返回值
print list_sort
print "下面是水果管理系统："
print "-------------------"
print "-------------------"

def checkfruits(fruit_check):
    checked = ["苹果","香蕉"]
    for i  in fruit_check :
        if i not in checked:
            checked.append(i)
    print "现有水果："
    checked.sort(reverse = True)
    for item in checked:
        print item
    return checked
fruit_list = ["苹果","栗子","李子","香蕉","桃子","西红柿"]
fruit_add = "猕猴桃"
fruit_list.append(fruit_add)
fruit_list = checkfruits(fruit_list)
fruit_search = "猕猴桃"
rank = fruit_list.index(fruit_search)+1
print '你要查找的水果：'+fruit_search+'在第'+str(rank)+'个'
tuple_mine = (2,3,4)
tuple_1,tuple_2,tuple_3 = tuple_mine
print tuple_1,tuple_2,tuple_3
print "直接遍历 tuple_mine:"
for it in tuple_mine:
    print it
print "通过range（len(tuple_mine))遍历 tuple_mine:"
for it2 in range(len(tuple_mine)):
    print tuple_mine[it2]
tuple_1 = (2,3,4)
tuple_2 = (6,7,8)
tuple_2D = (tuple_1,tuple_2)
print "遍历二维元组",tuple_2D
for i in range(len(tuple_2D)):
    for j in range(len(tuple_2D[i])) :
       print "tuple_2D["+str(i)+"]["+str(j)+"]=",tuple_2D[i][j]
print "通过map遍历元组:"
for i_map in map(None,tuple_2D) :
    print i_map
    for i  in i_map:
        print i
print "字典创建："
my_dic = {'4':'one','2':'two'}
print my_dic
my_dic.setdefault('8','eight')
my_dic.setdefault('2','eight')
print my_dic
my_dic['8'] = 'nine'
print my_dic
print list_sort
list_sort.remove(9)
print list_sort
del(list_sort[5])
print list_sort
print my_dic.items()    
for key in my_dic.iterkeys():
    print 'key='+key,'my_dic='+my_dic[key]
print my_dic
print "copy"
my_dic_copy = my_dic.copy()
print my_dic_copy
my_dic.clear()
print "clear "
print my_dic
print {}.fromkeys(['2','3'],[2,3])
print my_dic_copy.get('2'),my_dic_copy.get('10')
name = 'fan'
age = 12
print ("%s:%s"  %  (name,age))#非格式化输出
print list_sort
print "分片"
print list_sort[2:5]#[2,5)
print list_sort[-3:]
print list_sort[0::2]
print "字典的排序问题:"
dic_to_sort = {'a':9,'world':10,'z':8,'hello':12}
print sorted(dic_to_sort.items(),key = lambda d:d[0])
print sorted(dic_to_sort.items(),key = lambda d:d[1])
print " 测试ASCII转换："
num_ascii = 17
print num_ascii
print chr(num_ascii)
print ord(chr(num_ascii))
print "测试 join 和 split 函数"
string_str = 'i like program in python'
print string_str
print string_str.split()
seq = '~'
print seq.join(string_str.split())
print "测试strip函数"
str_strip = 'saaaayyey yes no yeyyaaaass'
print str_strip.strip('say')
print "左-右 第一个y坐标为%s" % str_strip.find("y")
print "右-左 第一个y坐标为%s" % str_strip.rfind("y")
print str_strip.replace("a","m",2)
import time
#import datetime
print time.strftime("%Y年%m月%d日%X",time.localtime())

class people:
    _myname = ' - -' 
    def __init__ (self,init_name):
        print "我是内置方法"
        self.__myname = init_name  
    def getname (self):
        print "我是普通方法,只能通过类的实例化对象才能够调用"
        print self.__myname
    @staticmethod
    def method_1 (__myname):
        print  __myname + "我是静态方法"+"可以用类名或者对象名称直接调用"
    @classmethod
    def class_method(cls, arvg):
        print "class_method(%s, %s)" % (cls, arvg)
        print "__myname=%s: " % cls._myname
    @classmethod
    def class_method2(arvg):
        print "class_method(%s)" % (arvg)
        #print "__myname=%s: " % cls.__myname
    def _name(self,__myname):
        print "我是私有方法" ,'myname = %s' %__myname
        
husky = people('dog')
husky.getname()
#people.method_1 ('static')
husky.method_1('static')
#people.__init__('husky')  X 
husky.__init__('husky') #  √
#people.classfuc (<class '__main__.people'>,'class')
people.class_method("Hello")
people.class_method2()
husky._name('__myname')
print husky._people__myname
print "-------------------------"
print "-------------------------"
print "-------------------------"       
print "-------------------------"
class test_new_init(object):
    def __new__ (self):
        print "__new__ "
    def __init__ (self):
        print "__init__ "
test_new_init_1 = test_new_init()
'''
在创建一个对象的时候，__new__方法会被最先调用，
然后会返回一个object实例；
在这之后，__init__方法才会被调用，
它不返回任何信息，只是初始化对象，
给对象的属性赋值。
'''
class nullclass:
    pass
def method_into (self):
    print "now i am in nullclass"
nullclass.getmethod = method_into
fuc = nullclass()
fuc.getmethod()
print "------------------------------"
print "------------------------------"
print "------------------------------"

class animal:
    """
    a class of animal
    """
    _feet = ' '
    _eye = ' '
    def __init__ (self,feet,eye):
        self._feet = feet
        self._eye = eye 
        print "animal de __init__ "
    def getfeet(self):
        print 'animal always have feet' + '   ' +self._feet
        return self._feet
    def geteye(self):
        print 'animal always have eyes' +'   ' +self._eye
        return self._eye
animal_one = animal('two feet','two eyes')
animal_one.getfeet()
animal_one.geteye()
class dog(animal):
    _bark = '汪汪'
    def __init__ (self):
        animal.__init__(self,'one','two')
        self._bark ='汪汪是狗特有的属性'
    def getbark (self):
        return self._bark        
dog_dogge = dog()
print dog_dogge.getbark()
def swap(x,y):
    x,y = y,x
    print 'x = %s ,y = %s ' % (x,y )
    return x>y
x = 5
y = 6
print swap(x, y)
#print 'x = %s ,y = %s ' % (x,y )
import random
rand_num = random.randrange(1,200,2)
print rand_num
print '\n'
print "oo"
import wx
print wx.version()
    
        

    
    
    
        
        
            
    

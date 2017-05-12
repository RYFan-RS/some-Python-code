#_*_ coding:utf-8 _*_
#中文注释
def fib(n):                   
    #print 'n =', n    #to get  n!        
    if n > 1:                 
        return n * fib(n - 1)
    else:                     
        #print 'end of the line'
        return 1
def sum2(a,b):
     """
     a function to sum up 2 number
     """
     print a+b
     return
name_ID = {"husky":4463,"bear":"2979"}
name_ID["flydog"]="0001"#增加一个元素对（键值对）
print name_ID["husky"] #允许使用不同数据类型在同一个dictionary 里面
print name_ID["bear"]
print name_ID
del name_ID["husky"]#删除一个元素对(键值对)
print name_ID
name_ID.clear()
print name_ID
print "list example"
list_1 = [1,12,3,4,5,6]
print list_1
list_2 = ['a','a','bb','jajdj','ehiad']
a="@".join(list_2)#join a string list
print a
print a.split("@")
print list_1[1:5]
list_1.append(0001)# reguard 0001  as 1 in the list
list_1.insert(2,90)
print list_1.index(90)
print list_1
list_1.remove(90)
print list_1
list_1+=list_1#list_1+list_1
print list_1
print 90 in list_1  #to make sure whather 90 is in list_1, wo know it is  false
#for i in range(7):
print sum(range(7))
s=1
for i in range(1,10):#cal mul amount 1 to 10
     s*=i
print s
if __name__=='__main__':  #main function in c/c++ 
     print(sum2.__doc__)

  
#_*_ coding:utf-8 _*_
import random
rand_num = [ ]
def get_rand_num():
    for i in range(0,10):
        rand_num.append(random.randrange(2,10000))
    print rand_num
    return
while True:
     num_1 = raw_input("请输入一个数字:").encode('utf-8')
     #num_1 = raw_input(u'请输入一个数字：'.encode('gbk')+'\n')#此处解决的换行符 中文编码乱码问
     get_rand_num()
     print rand_num[3]
     print float(num_1)*rand_num[3]
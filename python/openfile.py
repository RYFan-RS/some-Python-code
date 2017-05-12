#_*_ coding:utf-8 _*_
open_file = open("python.txt",'a+')
#open_file.write("open file in python")
readfile = open_file.read()
print readfile
print open_file.tell()
readline_file = open_file.readlines()
try:
    print "readline ok"
    for line in readline_file :
        print line
except:
    print "readline error "
open_file.close()

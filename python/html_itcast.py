#_*_ coding:utf-8 _*_
import urllib2
from pickle import dump

#url = r'https://www.sogou.com'
url  =  r'http://www.codefrom.com/paper/深入理解urllib、urllib2及requests'
#html = urllib2.urlopen(url).read()
user_agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
headers={'User_Agent':user_agent}

req=urllib2.Request(url,headers=headers)
html = urllib2.urlopen(req).read()
#new_html = html.decode("gbk").encode("utf-8") #error
new_html = html.decode('gbk', 'ignore').encode('utf-8') 
file_1=open('python.html','w')
#file_1.write("html")
#dump(html,file_1)
dump(new_html,file_1)
file_1.close()
print "ok"
print new_html
#print html
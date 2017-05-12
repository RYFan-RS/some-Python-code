import urllib2
 
url = r'http://www.baidu.com'
html = urllib2.urlopen(url).read()
 
print html
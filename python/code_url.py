import urllib2
url = 'http://www.runoob.com/python/python-tutorial.html'
response = urllib2.urlopen(url)
html =response.read()
print html
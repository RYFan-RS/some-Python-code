#_*_ coding:utf-8 _*_
import re

'''
refer to the code of Gábor Erds below
'''

N = "wherewhere"

cnt = 0
result = ''
countN = 0
showresult = []

for i in range(1,len(N)+1):
    if cnt <= len(re.findall(N[0:i],N)):
        cnt = len(re.findall(N[0:i],N))
        result = re.findall(N[0:i],N)[0]
        countN = len(N)/len(result)
        
for i in range(0,countN):
    showresult.append(result)
    
print showresult
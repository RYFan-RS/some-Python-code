import dbhash
db = dbhash.open('dbhashtemp','c')
db['西施'] = '西施浣纱'
db['貂蝉'] = '貂蝉拜月'
db['昭君'] = '昭君出塞'
print "没有进行任何操作："
for k,v in db.iteritems():
    print k,v
if db.has_key('西施'):
    del db['西施']
print "删除西施对应的数据："
for k,v in db.iteritems():
    print k,v  
db.close()
    


a={'id':'01','name':'a','dept':'ec','yearofpass':'2016','conduct':'good'}
b={'id':'02','name':'b','dept':'cs','yearofpass':'2016','conduct':'bad'}
c={'id':'03','name':'c','dept':'ee','yearofpass':'2015','conduct':'good'}
print "id : ",a['id'],b['id'],c['id']
print "name : ",a['name'],b['name'],c['name']
print "department : ",a['dept'],b['dept'],c['dept']
print "yop : ",a['yearofpass'],b['yearofpass'],c['yearofpass']
print "conduct : ",a['conduct'],b['conduct'],c['conduct']

del a['yearofpass']
print "afterdel :%s"% a.items()
d=a.copy()
e={'yearofpass':'2016'}
a.update(e)
print "afterupdate : %s"% a.items()
print "compreturn :%d" % cmp(a,b)
print "compreturn :%d" % cmp(b,c)
print "compreturn :%d" % cmp(a,d)
print "keys : %s"% a.keys()
del c





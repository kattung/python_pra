#!/usr/bin/python

s = [(1, 30), (30, 2)]

print "origin:", s

s.sort(key=lambda e:e[1])
print "sort by second column:", s

s.sort(key=lambda e:e[0])
print "sort by first column", s

mylist = []
interval = 333
weight = 0.3
mylist.append((interval, weight))

interval = 444
weight = 0.1
mylist.append((interval, weight))

interval = 222
weight = 0.4
mylist.append((interval, weight))
print mylist

mylist.sort(key=lambda e:e[0])
print "sort by the first element", mylist
mylist.sort(key=lambda e:e[0], reverse = True)
print "sort by the first element(reverse)", mylist

mylist.sort(key=lambda e:e[1])
print "sort by the second element", mylist

for item in mylist:
        ii = item[0]
        ww = item[1]
        print ii, ww

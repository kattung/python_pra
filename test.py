#!/usr/bin/python
"""
comment in many lines
many many lines
"""

import sys

class obj:
    file = None
    addr = None

def pass_arg(obj):
    obj.file = "bbb"

__obj = obj()
__obj.file = "aaa"
__obj.addr = 0x123
pass_arg(__obj)

print (__obj.file)

#one line comment

#number = 10
#add = number + 11
#print '45654', 'ppp', add, number
#print (), 'enter your name'

name = raw_input('enter your password ')
print name


### practice multi line

#msg = """one line
#two line
#three line"""
#
#print msg
#
#msg = "C:\\abcde\n efe"
#print msg

### concatenate string

"""
msg = "ppp"
msg2 = "bbb"
final = msg * 3
print final
final = msg + msg2
print final
print len(final)
print "123"*3
"""

#age = 16
#msg = "ttt"
#msg2 = str(age) + msg
#print msg2

### arithmetic
#a = 100
#print 100 / 3
#print 100 / 3.
#print float(a) / 3
#print float(a) // 3

### test list
#mylist = ["aaa", "bbb", "ccc", "ddd"]
#mylist.append('2000')
#print mylist
#mylist.extend("5000")
#print mylist
#print mylist[4]
#print mylist[1:4]
#mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print mylist[1][2]
#print mylist


#mylist = [1, 2, 3]
#mylist.append(4)
#mylist.extend([5, 6])
#print mylist
#mylist[3:5] = [3, 2, 7, 6, 8]
#print mylist


### dictionary
#mapping = {"one": "111", "two": "222", "three": "33"}
#print mapping
#print mapping["three"]
#print dict[2]
#mapping["two"] = "double two"
#print mapping["two"]
#qqq = mapping.copy()
#print qqq
#print qqq["one"]
#print qqq.keys()
#print qqq.values()


### print string
#string = ("abc", 123, "def", 123)
#print "%s %d %s %x" % string
##string = ["abc", 123, "def", 123]  #this is wrong
##print "%s %d %s %x" % string
#string = {"name": "qq", "age": 18}
#print "her name is %(name)s and age is %(age)d" % string
#print "her name is %(name)s" % {"name": "ppp"}


### if else
#pp = 2
#if (pp == 2) :
#    print "pp = %d" % pp
#elif (pp == 4) :
#    print "it's %d" % pp
#else:
#    print "no"
#    print "pp = %d" % pp


### loop
#for x in range(2, 100, 5):      # print 2 to 100, every 5 step
#    print x
#print "next"
#for x in range(2, 100, 5):
#    print x,                    # all numbers will be in the same line
#print                           # add a line break
#print                           # a blank line
#print "next line?"

#i = 0
#while (i < 10) :
#    print i
#    i += 1


### split and strip
#line = "   first ( second third   "
#print line
#item = line.split('(')
#print item
#line = line.strip()
#print line
#item = line.split()
#print item
#line = "      "
#print line
#item = line.split()
#print item


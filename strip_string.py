#!/usr/bin/python

s = '3.24%'
print "origin:", s
print "s[:-1]", s[:-1]    # equal to s[0:-1]

s = '01234567'
print "origin:", s
print "s[1:6]:", s[1:6]
print "s[0:-2]:", s[0:-2]

line = "   abcd, ssss   jjjj   "
print line
line = line.strip()
print line
line = line.split(",")
print line

pattern = 'abcd'
if pattern in line:
        print "ok"

#!/usr/bin/python

import sys
begin=int(sys.argv[1])
num=int(sys.argv[2])
line=sys.argv[3]
#line="111,222,333,444,555,666,777"
item=line.split(',')
print item

end=begin+num

for i in range(begin, end):
        print item[i]

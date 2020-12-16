#!/usr/bin/python

### This example work with use_save_here.py
### After this script save something in save_here.py
### "use_save_here.py" can use python list/dictionary in save_here.py

mylist = [ 1, 2, 3]
writefile = open("save_here.py", 'w')
writefile.write("mylist = %s" % mylist)

#!/usr/bin/python
import string
import os
import sys

abspath = os.path.abspath(sys.argv[0])
print "file: ", abspath

print "\ngetcwd() gives working directory (where you are)"
print "getcwd() => ", os.getcwd()
### basename will get filename without leading path
print "basename() => ", os.path.basename(sys.argv[0])
### dirname will get path, stripping out last one (path or file)
print "dirname of abspath => ", os.path.dirname(abspath)
print "call dirname() one more time, and it will strip one more path in front"
tmp = os.path.dirname(abspath)
print "dirname() again => ", os.path.dirname(tmp)


print "\nbelow is practice of relpath (relative path)"
print "relpath of input file and cwd => ", os.path.relpath(sys.argv[0])

### get relative path of two path
print "input two path, and relpath() will tell you their relative"
print "input file and katriona => ", os.path.relpath(sys.argv[0], "katriona")
print "input file and /home => ", os.path.relpath(sys.argv[0], "/home")
### it can give you ".."
print "/home and /home/katriona => ", os.path.relpath("/home", "/home/katriona")
print "/home/autotest/foo and /home/katriona => ", os.path.relpath("/home/autotest/foo", "/home/katriona")

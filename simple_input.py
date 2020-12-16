#!/usr/bin/python
import sys


input_len = len(sys.argv)
if input_len < 3:
        print "please enter two argument"
        exit()
print "len(sys.argv) = ", input_len
print "sys.argv", sys.argv

for i in range(0, input_len):
        pattern = "sys.argv[" + str(i) + "] ="
        print pattern, sys.argv[i]

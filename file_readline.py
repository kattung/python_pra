#!/usr/bin/python
import readline

read_file = open("text.txt")

# read first line only
print "### read first line only"
line = read_file.readline()
print line

# read each line, but this will continue to read
print "### read following lines"
for line in read_file.readlines():
        print line

print "### to re-read the whole file, you have to reopen the file"
read_file = open("text.txt")
for line in read_file.readlines():
        print line
read_file.close()

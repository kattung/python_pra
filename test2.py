#!/usr/bin/python
import string


my_hexdata = "1aad1342"
num_of_bits = 32

#print(bin(int(my_hexdata, 16))[2:].zfill(num_of_bits))

f = open('text.txt')
lines = f.readlines()
#lines.split()
print(lines)
f.close

#file = open('text.txt')
#a = file.readline().split()
#print(a)
#numbers = string.atoi(file.readline().split())

#!/usr/bin/python
import os

path = "/home/katriona/practice/python_practice"
file_list = os.listdir(path)
for f in file_list:
        if f.endswith(".py"):
                print f

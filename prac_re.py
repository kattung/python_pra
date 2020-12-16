#!/usr/bin/env python
import re

def match_pattern(string):
    print("check string %s" % string)
    mymatch = re.compile(r"aaa (\d) bbb.(\w+)")
    m = mymatch.match(string)
    if m:
        print("MATCH:")
        print m.group(1)
        print m.group(2)

match_pattern("aaa 123 bbb.klk")
match_pattern("aaa 1 bbb.klk")

#!/usr/bin/env python

class ext_mode():
    none = 0
    sec = 1
    ns = 2
    hyp = 3

def check_mode(mode):
    if mode == ext_mode.hyp:
        print("hyp mode")
    elif mode == ext_mode.ns:
        print("non secure mode")

check_mode(ext_mode.ns)
check_mode(ext_mode.hyp)

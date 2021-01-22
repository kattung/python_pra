#!/usr/bin/python

import my_module

### import customized module from different path
import sys
import os.path as osp
cmd_dir = osp.join(osp.dirname(__file__), "cmd")
sys.path.append(cmd_dir)
import common

my_module.printhello("abc")
my_module.adder(4, 5)
print my_module.mult(43, 5)

print(common.linux_banner)

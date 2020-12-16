#!/usr/bin/env python
import sys
import subprocess

if len(sys.argv) > 1:
    sys.exit("error")

print "pass"


print "\ncall ./sort.py"
process = subprocess.Popen("./sort.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
stdout, stderr = process.communicate()
if stderr is not "":
    print stderr
print stdout


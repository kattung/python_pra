#!/usr/bin/python
from subprocess import call
import subprocess

#print "call ./test.sh"
#out_pattern = "hello"
#call(["./test.sh", out_pattern])
#
#print "\ncall ./sort.py"
#call(["./sort.py"])
#
#print "\ncall ./sort.py"
#call("./sort.py", shell=True)

### use popen to get stdin/stdout/stderr
print "\nTest popen"
process = subprocess.Popen("./print_error.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
stdout, stderr = process.communicate()
if stderr is not "":
    print stderr
print stdout


print "\nTest popen"
process = subprocess.Popen("./print_error.py 1",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)
stdout, stderr = process.communicate()
if stderr is not "":
    print stderr
print stdout

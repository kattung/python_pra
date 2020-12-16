#!/usr/bin/env python
import pexpect
from subprocess import call

def cowsay_ascii_art(string):
    pattern = r'''
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\
             U  ||----w |
                ||     ||
'''
    string_len = len(string)
    underline = " "
    dash = " "
    for i in range(0, string_len):
        underline += "_"
        dash += "-"
    print underline
    print "<", string, ">"
    print dash, pattern

def check_cowsay_available():
    input_args = []
    input_args.append("hello world")
    exp_prompt = "hello"

    __pxqu = pexpect.spawn('cowsay', input_args)
    ret = __pxqu.expect([exp_prompt, pexpect.TIMEOUT, pexpect.EOF])

    if ret != 0:
        print "sadly. you don't have cowsay!!"
        print "we will use ascii art instead!!"
        cowsay_ascii_art("Like this? ^^ ")
    else:
        pattern = "good. you have cowsay!!"
        call(["cowsay", pattern])

def main():
    check_cowsay_available()

if __name__ == "__main__":
    main()

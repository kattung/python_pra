#!/usr/bin/env python
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
    try:
        pattern = "good. you have cowsay!!"
        call(["cowsay", pattern])
    except:
        print "Sadly. you don't have cowsay!!"
        print "We will use ascii art instead!!"
        cowsay_ascii_art("Like this? ^^ ")


def main():
    check_cowsay_available()

if __name__ == "__main__":
    main()

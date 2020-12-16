#!/usr/bin/env python
import argparse
import ConfigParser

class bootargs:
    pass
__bootargs = bootargs()

def parse_args():
    parser = argparse.ArgumentParser(description =
        "This script give example of using ini.  \
         Example: ./get_ini.py -i example.ini   \
        ")
    parser.add_argument('-i', '--ini', required = True)
    return parser.parse_args()

def parse_ini(ini):
    config = ConfigParser.ConfigParser()
    config.read(ini)
    ### get bootargs
    __bootargs.ttynode = config.get('bootargs', 'ttynode').strip('"')
    __bootargs.console = config.get('bootargs', 'console').strip('"')
    __bootargs.append = config.get('bootargs', 'append').strip('"')

    print "ttynode: ", __bootargs.ttynode
    print "console: ", __bootargs.console
    print "append: ", __bootargs.append

def main():
    args = parse_args()
    parse_ini(args.ini)

if __name__ == "__main__":
    main()

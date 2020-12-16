#!/usr/bin/env python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description ='''
Practice of argparse metavar. Please try the following:
./metavar -sim aaa
./metavar -sim bbb
./metavar -sim ccc
./metavar
./metavar -sim
            ''')
    #parser.add_argument('-sim', '--simpoint', metavar=('aaa' or 'bbb'),
    parser.add_argument('-sim', '--simpoint', metavar="<aaa|bbb>",
            help = "please input 'aaa' or 'bbb'")
    return parser.parse_args()

def main():
    __args = parse_args()
    if __args.simpoint == 'aaa':
        print "got aaa"
    elif __args.simpoint == 'bbb':
        print "got bbb"
    else:
        print __args.simpoint

if __name__ == "__main__":
    main()

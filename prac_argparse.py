#!/usr/bin/python
import argparse
import sys

def foo():
        print "foo"

def parse_args():
        parser = argparse.ArgumentParser(description =
                        "Practice of input parse")
        parser.add_argument('-i', '--input_file', required = True,
                        help = "input file")
        parser.add_argument('-o', '--output',
                        help = "outpu file")
        parser.add_argument('-f', '--flag', action="store_true",
                        help = "flag. if set, call function foo")
        parser.add_argument('-p', '--plus_arg', nargs=2,
                        help = "plus argument, if set, two arguments shoule be given")
        parser.add_argument('--name', metavar="<aaa|bbb>",
                        help = "specify name to be 'aaa' or 'bbb'.\
                        metavar is used to show option for the argument. \
                        but if you specify another name, it is also acceptable.\
                        you can add checking rule by yourself.\
                        ")
        return parser.parse_args()

def main():
        args = parse_args()
        print("Print input: ")
        print(" ".join(sys.argv))
        input_file = args.input_file
        print "input", input_file
        if args.output is not None:
                print "output", args.output
        if args.plus_arg is not None:
                plus_arg = args.plus_arg
                print "plus argument1", plus_arg[0]
                print "plus argument2", plus_arg[1]
        if args.flag:
                foo()

        if args.name:
            print args.name
            if args.name is not 'aaa' or args.name is not 'bbb':
                print "error: you can only input 'aaa' or 'bbb' for --name"

if __name__ == "__main__":
        main()

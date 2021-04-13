#!/usr/bin/env python3
import argparse

class run:
    aa = 0
    bb = 0

def parse_args():
    parser = argparse.ArgumentParser(description =
            "Practice of logging")
    parser.add_argument('-v', '--verbose', action = 'store_true',
            help = "print debug message")
    parser.add_argument('-e', '--error', action = 'store_true',
            help = "print error message")
    return parser.parse_args()

def my_print():
    global __args

    print("first: %s" % __args.test1)
    print("run: %s" % __args.run.aa)

    __args.run.aa = 1
    print("run: %s" % __args.run.aa)

def main():
    global __args

    __args = parse_args()

    __args.test1 = "test1"

    __args.run = run()
    my_print()

if __name__ == "__main__":
    main()

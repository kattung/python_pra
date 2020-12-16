#!/usr/bin/env python
import logging
import argparse
import sys
import time

pr_info = logging.info
pr_debug = logging.debug
__args = None

def parse_args():
    parser = argparse.ArgumentParser(description =
            "Practice of logging")
    parser.add_argument('-v', '--verbose', action = 'store_true',
            help = "print debug message")
    parser.add_argument('-e', '--error', action = 'store_true',
            help = "print error message")
    return parser.parse_args()

def logging_init():
    if __args.verbose is True:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(format='%(message)s',level = level)

def main():
    global __args

    __args = parse_args()
    logging_init()
    pr_info("<<<<<<<< part3: print info")
    pr_debug("<<<<<<<< part3: print debug")
    time.sleep(3)
    if __args.error is True:
        sys.exit("<<<<<<<< part3: exception occurs!!")
    pr_info("<<<<<<<< part3: after error message")

if __name__ == "__main__":
    main()

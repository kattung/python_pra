#!/usr/bin/env python3
import logging
import argparse
import sys

pr_info = logging.info
pr_debug = logging.debug
pr_error = logging.error

def pr_err_exit(string):
    pr_error(string)
    sys.exit(1)

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
    logging.basicConfig(format='%(message)s',
            level = level,
            handlers = [
                logging.FileHandler("debug.log"),
                logging.StreamHandler(),
                ]
            )


def main():
    global __args

    __args = parse_args()
    logging_init()
    pr_info("print info")
    pr_debug("print debug")
    if __args.error is True:
        pr_err_exit("exception occurs!!")
    pr_info("after test error message")

if __name__ == "__main__":
    main()

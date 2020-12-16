#!/usr/bin/env python
import logging
import argparse
import sys
import time
import subprocess

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

def work():
    if __args.verbose is True:
        verbose = "-v"
    else:
        verbose = ""

    part3_err = 1
    if part3_err == 1:
        error = "-e"
    else:
        error = ""

    script = "./logging_part3.py"
    command = "%(script)s %(verbose)s %(error)s" % {
            'script': script,
            'verbose': verbose,
            'error': error,
            }
    ret = subprocess.call(command, shell = True)
    if ret == 1:
        sys.exit("part2: part3 fail!!")


def main():
    global __args

    __args = parse_args()
    logging_init()
    pr_info("part2: print info")
    pr_debug("part2: print debug")
    time.sleep(3)
    if __args.error is True:
        sys.exit("part2: exception occurs!!")
    pr_info("part2: after error message")
    work()
    pr_info("part2: after call part3")

if __name__ == "__main__":
    main()

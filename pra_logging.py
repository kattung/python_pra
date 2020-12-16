#!/usr/bin/env python
import logging
import argparse
import sys
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
    logging.basicConfig(format='%(levelname)-8s: %(message)s',level = level)

def work():
    """
    Let's call logging_part2.py
    And see how the output goes
    """
    if __args.verbose is True:
        verbose = "-v"
    else:
        verbose = ""

    part2_err = 0
    if part2_err == 1:
        error = "-e"
    else:
        error = ""

    script = "./logging_part2.py"
    command = "%(script)s %(verbose)s %(error)s" % {
            'script': script,
            'verbose': verbose,
            'error': error,
            }
    ret = subprocess.call(command, shell = True)
    if ret == 1:
        sys.exit("ERROR: part2 fail!!")

def main():
    global __args

    __args = parse_args()
    logging_init()
    pr_info("print info")
    pr_debug("print debug")
    work()
    pr_info("after calling part2")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import argparse
import os
import os.path as osp
import readline
import re
import sys
import logging
import time
import serial
import pexpect
from pexpect import fdpexpect

pr_info = logging.info
pr_debug = logging.debug
pr_error = logging.error

def pr_err_exit(string):
    pr_error(string)
    sys.exit()

def logging_init():
    if __args.verbose is True:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(format = "%(levelname)-8s: %(message)s", level = level)

def parse_args():
    parser = argparse.ArgumentParser(
	formatter_class=argparse.RawTextHelpFormatter,
	description = '''
This script will do the following
1. open uart
2. enter command to run test
3. save log
''')
    parser.add_argument('-p', '--port',
            default = "/dev/ttyUSB0",
            help = "uart port. default: /dev/ttyUSB0")
    parser.add_argument('-l', '--log',
            default = "uart.log",
            help = "uart log file. default: ./uart.log")
    parser.add_argument('-v', '--verbose', action = 'store_true',
            help = "print debug message")
    return parser.parse_args()

def check_file_exist(filename):
    if not osp.exists(filename):
        pr_err_exit("file not found: %s" % filename)

def sanity_test():
    if __args.log:
        check_file_exist(__args.log)

def write_log(string):
    tmp1 = string.decode("utf-8")
    tmp2 = re.sub('\x1b\[[0-9;]*m', '', tmp1)
    tmp3 = re.sub('\x1b\(B', '', tmp2)
    string = re.sub('\a\b\r', '', tmp3)
    __args.out.write(string)

def send_cmd(cmd, expt, timeout):
    ser = __args.ser
    uart = fdpexpect.fdspawn(ser.fileno())
    uart.send(cmd + "\r\n")
    ret = uart.expect([expt, pexpect.TIMEOUT], timeout=timeout)
    pr_debug("send command: %s" % cmd)

    if ret == 0:
        pr_debug("found match: %s" % expt)
        write_log(uart.before)
        write_log(uart.after)
    elif ret == 1:
        write_log(uart.before)
        pr_error("")
        pr_error("Fail to get expected pattern")
        pr_error("command: %s" % cmd)
        pr_err_exit("exptected pattern: %s" % expt)

def open_uart():
    global __args

    print("open_uart")
    ser = serial.Serial(__args.port, baudrate = 115200, timeout = 1)
    __args.ser = ser


def close_uart():
    __args.ser.close()

def work():
    global __args

    output = open(__args.log, "w")
    __args.out = output

    open_uart()
    send_cmd("ls /bin", "# ", 3)
    send_cmd("ls /dev", "abc", 6) ## this will cause timeout
    close_uart()

    output.close()


def main():
    global __args

    __args = parse_args()

    logging_init()
    #sanity_test()
    work()


if __name__ == "__main__":
    main()

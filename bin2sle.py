#!/usr/bin/env python

import sys
import os.path
import gzip
import struct
import getopt

class args:
    pass
__args = args()

BLOCK_SIZE = 2**10

def usage():
    message = """\
usage: %s [-h] -i input_file [-o output_name]
            [-a load_addr] [-u instance]

This script will convert binary to sle ddr format.
The interleave processing will place
the first 64 byte data to channel 0, and the next 64 byte to channel 1

optional arguments:
  -h, --help        show this help message and exit
  -i input          input binary file
  -o output_name    name of output file
                    <output_name>.chn0.sle
                    <output_name>.chn1.sle
                    If '-o' is not specified,
                    the name will take input file without '.bin' or '.gz'
  -a load_addr      address to load binary, default: 0x0
                    the address will be divided by two to fit the memory instance
  -u instance       the memory instance to load binary
                    default: U_mt41j6m16_CS0.memcore
"""
    print(message % sys.argv[0])

def gen_header(idx_base, idx_end):
    global __args
    header_template = """\
$INSTANCE   %(instance)s
$RADIX  HEX
$ADDRESS    %(start)x    %(end)x
"""
    header = header_template % {
            'instance': __args.instance,
            'start': idx_base,
            'end': idx_end
            }
    return header

def __convert(_bin, _ch0, _ch1):
    global __args

    idx_base = int(__args.addr, 16) / 2
    ch0_idx = idx_base
    ch1_idx = idx_base
    ch0_word = ''
    ch1_word = ''
    addr = 0

    while True:
        words = _bin.read(BLOCK_SIZE)
        if words == '':
            break
        for i in xrange(0, len(words), 4):
            w = words[i:i+4]
            (n, ) = struct.unpack("I", w)
            if (addr & 0x40):
                ch1_word += ('%08x\t%x\n' % (ch1_idx, n))
                ch1_idx += 1
            else:
                ch0_word += ('%08x\t%x\n' % (ch0_idx, n))
                ch0_idx += 1
            addr += 4

    ch0_header = gen_header(idx_base, ch0_idx-1)
    ch1_header = gen_header(idx_base, ch1_idx-1)
    _ch0.write(ch0_header)
    _ch0.write(ch0_word)
    _ch1.write(ch1_header)
    _ch1.write(ch1_word)

def convert(bin_file, ch0_file, ch1_file):
    try:
        if bin_file.endswith(".gz"):
            bin_file = gzip.open(bin_file, "rb")
        else:
            bin_file = open(bin_file, "rb")
        ch0_file = open(ch0_file, "w")
        ch1_file = open(ch1_file, "w")
        __convert(bin_file, ch0_file, ch1_file)
    finally:
        if bin_file is not None:
            bin_file.close()
        if ch0_file is not None:
            ch0_file.close()
        if ch1_file is not None:
            ch1_file.close()

def strip_suffix(string):
    suffix_list = [".bin.gz", ".bin", ".gz", ".dtb"]
    suffix = None
    for item in suffix_list:
        if string.endswith(item):
            suffix = item
            break

    if suffix:
        result = string[:len(string) - len(suffix)]
    else:
        result = string
    return result

def parse_args():
    global __args

    if sys.argv[1] == "--help" :
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:a:u:")
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit()

    for o, a in opts:
        if o == "-h":
            usage()
            sys.exit()
        elif o == "-i":
            __args.input_file = a
        elif o == "-o":
            __args.output_name = a
        elif o == "-a":
            __args.addr = a
        elif o == "-u":
            __args.instance = a

    if hasattr(__args, 'input_file') is False:
            usage()
            sys.exit()

    if os.path.isfile(__args.input_file) is not True:
        sys.exit("ERROR: file %s not exist" % __args.input_file)

    if hasattr(__args, 'addr') is False:
        __args.addr = "0"

    if hasattr(__args, 'instance') is False:
        __args.instance = "U_mt41j6m16_CS0.memcore"


def main():
    parse_args()

    if hasattr(__args, 'output_name'):
        output_name = __args.output_name
    else:
        output_name = strip_suffix(__args.input_file)

    ch0_file_name = output_name + ".chn0.sle"
    ch1_file_name = output_name + ".chn1.sle"
    convert(__args.input_file, ch0_file_name, ch1_file_name)

if __name__ == '__main__':
    main()

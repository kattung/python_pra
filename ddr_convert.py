#!/usr/bin/env python

import sys
import os.path
import gzip
import struct

BLOCK_SIZE = 8 * 2**10

def usage():
    message = """\
Usage: %s input_file [output]
name of output file will be <output>.ddr
If 'output' is not specified,
output name will be input_file_name without '.bin' or '.gz'\
"""
    print(message % sys.argv[0])

def __convert(_bin, _out):
    while True:
        words = _bin.read(BLOCK_SIZE)
        if words == '':
            break

        words += (BLOCK_SIZE - len(words))*'\x00'

        new_word = ''
        for i in xrange(0, BLOCK_SIZE, 4):
            w = words[i:i+4]
            (n, ) = struct.unpack("I", w)
            new_word += '0x%08x\n' % n
        _out.write(new_word)

def convert(bin_file, out_file):
    try:
        if bin_file.endswith(".gz"):
            bin_file = gzip.open(bin_file, "rb")
        else:
            bin_file = open(bin_file, "rb")
        out_file = open(out_file, "w")
        __convert(bin_file, out_file)
    finally:
        if bin_file is not None:
            bin_file.close()
        if out_file is not None:
            out_file.close()

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

def main():
    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help" :
        usage()
    else:
        bin_file_name = sys.argv[1]
        if os.path.isfile(bin_file_name) is not True:
            print("file not exist: %s" % bin_file_name)
            sys.exit()
        if len(sys.argv) == 3:
            output_name = sys.argv[2]
        else:
            output_name = strip_suffix(bin_file_name)

        out_file_name = output_name + ".ddr"
        convert(bin_file_name, out_file_name)

if __name__ == '__main__':
    main()

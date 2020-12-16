#!/usr/bin/env python
import argparse
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description =
            "test dictzip")
    parser.add_argument('-p', '--path', required = True,
            help = "path contains binary")
    return parser.parse_args()

def work(path):
    command = "dictzip %s/*.bin" % path
    print command
    subprocess.call(command, shell=True)

def main():
    args = parse_args()
    work(args.path)

if __name__ == "__main__":
    main()

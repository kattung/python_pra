#!/usr/bin/env python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description = '''
Here I can have more clear help message
1. I can control anything as I want
    a. like this
            ----
2. This is very good

Note: if you use RawDescriptionHelpFormatter instead of RawTextHelpFormatter
only descrition can be indent
'''
            )
    parser.add_argument('-a',
            help = "original argument help")
    parser.add_argument('-b',
            help = ('''\
Test indent in argument help.
    could this be indent???
    yes!!! ^^
''')
            )
    return parser.parse_args()


def main():
    args = parse_args()

if __name__ == "__main__":
    main()

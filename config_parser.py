#!/usr/bin/env python
import argparse
import os.path as osp
import ConfigParser

def parse_args():
    parser = argparse.ArgumentParser(
            description = "practice parser config")
    parser.add_argument('-i', '--input', required = True)
    return parser.parse_args()

def main():
    __args = parse_args()
    if osp.isfile(__args.input) is None:
        print("File %s not exist" % __args.input)

    config = ConfigParser.ConfigParser()
    config.read(__args.input)

    aaa = config.get('people', 'aaa')
    print("in section 'people', there is a name 'aaa' with value %s" % aaa)
    print(config.items('like'))

    ### check if has_section
    print(config.has_section('like'))
    ### check if has_option
    print(config.has_option('like', 'sport'))
    sport = config.get('like', 'sport')

    ### remove option
    config.remove_option('like', 'sport')
    ### modify exist option
    config.set('like', 'sport', sport)

    ### write back
    print("modify ini file")
    ini = open(__args.input, 'w')
    config.write(ini)
    print("Please note that command in ini file will be removed")

if __name__ == "__main__":
    main()

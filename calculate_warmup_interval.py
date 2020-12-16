#!/usr/bin/python
### This script shoule be placed in spec_score_analysis/script
import argparse
import readline
import os
import sys
import common

dict_interval = {}
dict_weight = {}
dict_total_interval = {}
dict_phase_num = {}

default_warmup = 4
use_default = 0
dict_warmup = {}

def work(spec_list, out_file):
        total_spec_num = 0
        total_interval_num = 0

        read_file = open(spec_list, 'r')
        write_file = open(out_file, 'w')
        for line in read_file.readlines():
                total_spec_num += 1
                testcase = line.strip('\n')
                total_interval = dict_total_interval.get(testcase)
                phase_num = dict_phase_num.get(testcase)
                phase_num = int(phase_num)

                # get warmup interval
                if use_default:
                        warmup_interval = default_warmup
                else:
                        warmup_interval = dict_warmup.get(testcase)
                        if warmup_interval is None:
                                warmup_interval = default_warmup
                warmup_interval = int(warmup_interval)

                pattern = testcase + "," + str(phase_num) + "," + str(warmup_interval) + "\n"
                write_file.write(pattern)
                total_interval_num += int(phase_num) * int(warmup_interval)

        read_file.close()

        write_file.write("total spec number: " + str(total_spec_num))
        write_file.write("\ntotal warmup interval number: ")
        write_file.write(str(total_interval_num))
        write_file.close()


def parse_log(filename, dictionary):
        common.check_file_exist(filename, None)
        read_file = open(filename, 'r')
        for line in read_file.readlines():
                lineline = line.split(",")
                name = lineline[0]
                value = lineline[1].strip("\n")
                dictionary.update({name: value})
        read_file.close()

def gen_dict(interval_file, weight_file, total_interval_file, phase_num_file):
        parse_log(interval_file, dict_interval)
        parse_log(weight_file, dict_weight)
        parse_log(total_interval_file, dict_total_interval)
        parse_log(phase_num_file, dict_phase_num)

def parse_args():
        parser = argparse.ArgumentParser(description =
                        "This script will generate information \
                         to build checkpoint"
                        )
        parser.add_argument('--spec', required = True,
                        help = "spec2000_int, spec2000_fp, spec2006_int")
        parser.add_argument('-o', '--output', required = True,
                        help = "output file")
        return parser.parse_args()

def main():
        global use_default
        args = parse_args()
        spec = args.spec
        out_file = args.output

        base_dir = common.get_basedir(sys.argv[0])
        simpoint_path = base_dir + "/spec_info/simpoint_info/" + spec
        interval_file = simpoint_path + "/interval.txt"
        weight_file = simpoint_path + "/weight.txt"
        total_interval_file = simpoint_path + "/total_interval.txt"
        phase_num_file = simpoint_path + "/phase_num.txt"
        gen_dict(interval_file, weight_file, total_interval_file,
                        phase_num_file)

        warmup_file = base_dir + "/data/warmup/" + spec + "/warmup_interval.txt"
        if os.path.isfile(warmup_file) is not True:
                use_default = 1
        else:
                parse_log(warmup_file, dict_warmup)

        spec_list = base_dir + "/spec_info/spec_list/" + spec + ".testcase"
        common.check_file_exist(spec_list, None)
        work(spec_list, out_file)

if __name__ == "__main__":
        main()

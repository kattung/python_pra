#!/usr/bin/python
import sys
import argparse
import readline
import re
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from xlsxwriter.utility import xl_range

spec_info_title = ["interval", "weight" , "cycle" , "cycle", "cycle",
                   "average", "phase_num", "total_interval"];
skip_pattern = ["total cycle", "total interval"];

golden_exp_iter = 3
golden_cycle_col_start = 2
spec_info_phase_col = 6
spec_info_interval_col = 7

def write_title(writesheet, pattern, row):
        col = 0
        for item in pattern:
                writesheet.write(row, col, item)
                col += 1

# get testcase name from spec_list
def get_testcase(spec, testcase):
        filename = "./spec_list/" + spec + ".testcase"
        spec_list = open(filename, 'r')
        for line in spec_list.readlines():
                line = line.strip()
                if not len(line) or line.startswith('#'):
                        continue
                testcase.append(line)
        spec_list.close

# calculate average and write to worksheet
def write_average(writesheet, row, col, ave_col_start, ave_col_end):
        cell_range = xl_range(row, ave_col_start, row, ave_col_end)
        formula = '=AVERAGE(' + cell_range + ')'
        writesheet.write(row, col, formula)

# extract cycle count of each checkpoint from runrun log
def get_golden_cycle(writesheet, testcase, args, interval, row, col):
        col += golden_cycle_col_start
        col_start = col
        for i in range(0, golden_exp_iter):
                filename = args.gen_golden[0] + "/log" + str(i) + "/" + testcase + ".log"
                runrun_log = open(filename, 'r');
                for line in runrun_log.readlines():
                        pattern = "runrun " + interval + ":"
                        if pattern in line:
                                tmp1 = line.split("runrun")
                                tmp2 = tmp1[1].split(" ")
                                cycle = tmp2[2]
                                writesheet.write_number(row, col, int(cycle))
                                col += 1
                                break

        # calculate average
        col_end = col - 1
        write_average(writesheet, row, col, col_start, col_end)

# calculate total cycle count
def cal_total_cycle(writesheet, testcase, args, row):
        col = 0
        writesheet.write(row, col, "total cycle")

        col = golden_exp_iter - 1
	p = re.compile(".*runrun (\d+): (\d+) cycles passed")
        for i in range(0, golden_exp_iter):
                filename = args.gen_golden[0] + "/log" + str(i) + "/" + testcase + ".log"
                logfile = open(filename)
                index = 0
                total_cycle = 0
	        for line in logfile:
		        m = p.match(line)
		        if not m:
			        continue
		        (n, cycle) = m.group(1, 2)
                        if int(n) != index:
                                print "Error:", filename, ": Interval", index, "is missing"
                                print n
			        exit()
                        total_cycle += int(cycle)
                        index += 1
                writesheet.write_number(row, col, total_cycle)
                logfile.close()
                col += 1

def write_golden_info(spec, writesheet, testcase, args):
        row = 0
        write_title(writesheet, spec_info_title, row)

        # get simpoint information
        filename = "./spec_simpoint_info/" + spec + "/" + testcase + ".simpoint"
        simpoint_file = open(filename, 'r')
        row = 1
        for line in simpoint_file.readlines():
                col = 0
                for item in line.split(' '):
                        if col == 0:
                                writesheet.write_number(row, col, int(item))
                                get_golden_cycle(writesheet, testcase, args,
                                                item, row, col)
                        elif col == 1:
                                writesheet.write_number(row, col, float(item))
                        else:
                                continue
                        col += 1
                row += 1
        last = line.split(' ')
        total_interval = last[2].strip()
        simpoint_file.close()

        cal_total_cycle(writesheet, testcase, args, row)
        col_start = golden_cycle_col_start
        col = col_start + golden_exp_iter
        col_end = col - 1
        write_average(writesheet, row, col, col_start, col_end)

        ret_value = []
        phase_num = row - 1
        ret_value.append(phase_num)
        ret_value.append(int(total_interval))
        return ret_value

def gen_spec_info_sheet(spec, testcase, excel, args):
        print "Generate SIMPOINT and golden cycle information"

        specinfo_sheet = excel.add_worksheet("spec_info")
        ret = write_golden_info(spec, specinfo_sheet, testcase, args)
        specinfo_sheet.write_number(1, spec_info_phase_col, ret[0])     # phase_num
        specinfo_sheet.write_number(1, spec_info_interval_col, ret[1])  # total_interval

def parse_args():
        parser = argparse.ArgumentParser(description =
                "This script will gather cycle count for each checkpoint. \
                And then reconsturct spec score according to SIMPOINT phase weight. \
                Finally, compare them with golden cycle. (i.e. Exynos)")
        parser.add_argument('--spec', required = True,
                        help = "spec2000_int, spec2000_fp, spec2006_int")
        parser.add_argument('-o', '--output_path', required = True,
                        help = "The path of excel file for each test case analysis")
        parser.add_argument('-g', '--gen_golden', nargs=1,
                        help = "Generate SPEC SIMPOINT information and golden cycle count.\
                                If the information exist, skip this action.             \
                                Argument: cycle_folder_top_path                         \
                                (three folders log0/ log1/ and  log2/ should be in this path)     \
                        ")
        return parser.parse_args()


def main():
        args = parse_args()
        output_path = args.output_path
        spec = args.spec

        testcase = list()
        get_testcase(spec, testcase)

        for item in testcase:
                print item
                filename = output_path + "/" + item + ".xlsx"
                excel = xlsxwriter.Workbook(filename)

                if args.gen_golden is not None:
                        gen_spec_info_sheet(spec, item, excel, args)

                excel.close()

if __name__ == "__main__":
        main()

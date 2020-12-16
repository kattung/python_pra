#!/usr/bin/env python
### This practice is for checkpoint generation
### Some checkpoint may do checkpoint at the same interval (index 0)
### We skip doing checkpoint that that interval
### And then do post preprocess, to create nessacery files for the skipping intervals
### Also, we rename existed files to avoid overwriting
### Example: target interval: 0, 2, 100
###    => interval to do checkpoint with 4 warmup interval: 0, 96
###    After ckeckpoint is generated, we have files for index0 and index1
###    We have to rename files of index1 to index2, and then copy files of index0 to index1

import os
import os.path as osp
import shutil

def strip_prefix(string, prefix):
    return string[len(prefix):len(string)]


def split_ckp_filename(filename, prefix):
    latter = strip_prefix(filename, prefix)
    latter_split = latter.split('.')
    index = latter_split[0]
    last_part = strip_prefix(latter, index)
    return (index, last_part)

def gen_dec_filelist(file_list, prefix, suffix):
    new_list = []
    for i in file_list:
        if i.endswith(suffix):
            (index, last_part) = split_ckp_filename(i, prefix)
            filename = (prefix, int(index), last_part)
            new_list.append(filename)

    new_list.sort(key=lambda e:e[1], reverse = True)
    return new_list


def rename_file(path, prefix, suffix, orig_skip_num):
    file_list = os.listdir(path)
    dec_file_list = gen_dec_filelist(file_list, prefix, suffix)
    for (p, i, l) in dec_file_list:
        orig = p + str(i) + l
        if i == 1:
            print '%s unchanged' % orig
            continue
        new_index = i + orig_skip_num
        new_name = p + str(new_index) + l
        print 'rename %s to %s'  % (orig, new_name)
        src = osp.join(path, orig)
        dst = osp.join(path, new_name)
        os.rename(src, dst)

def copy_files(path, copy_base, num, prefix):
    begin = 2
    end = 2 + num
    (index, last_part) = split_ckp_filename(copy_base, prefix)
    for i in range(begin, end):
        copy = prefix + str(i) + last_part
        print 'copy %s to %s' % (copy_base, copy)
        src = osp.join(path, copy_base)
        dst = osp.join(path, copy)
        shutil.copyfile(osp.abspath(src), osp.abspath(dst))

def copy_ckp1(path, prefix, orig_skip_num):
    file_list = os.listdir(path)
    ckp1 = prefix + '1'
    for i in file_list:
        if i.startswith(ckp1):
            copy_files(path, i, orig_skip_num, prefix)

def rename_output_files(path, skip_num):
    prefix = 'ckp-vcpu-'
    rename_file(path, prefix, '.ini', skip_num)
    rename_file(path, prefix, '.bin.dz', skip_num)
    copy_ckp1(path, prefix, skip_num)

def main():
    path = '/home/katriona/tmp/checkpoint/specrand_base'
    skip_num = 1
    rename_output_files(path, skip_num)

if __name__ == '__main__':
    main()

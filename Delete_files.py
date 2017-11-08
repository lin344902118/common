# -*- coding:utf-8 -*-
"""
    this is a program to delete specify files
"""

import os
import sys
import getopt

def usage():
    print 'this is a program to delete all specified files in the specified path\n' \
          '-h --help show this usage\n' \
          '-f --filename delete all files start with this filename, such as test or pyc, if not specified, delete all files\n' \
          '-p --path delete files from the specified path\n'

def get_argument():
    try:
        path = ''
        filename = ''
        opts, args = getopt.getopt(sys.argv[1:], 'hf:p:', ['--help', '--filename', '--path'])
        for o, a in opts:
            if o in ['-h', '--help']:
                usage()
                sys.exit()
            if o in ['-f', '--filename']:
                filename = a
            if o in ['-p', '--path']:
                path = a
        if filename:
            delete_files_with_filename(path, filename)
        else:
            delete_all_files(path)
    except getopt.GetoptError:
        usage()
        sys.exit()

def delete_files_with_filename(path, filename=None):
    del_list = os.listdir(path)
    for f in del_list:
        filepath = os.path.join(path, f)
        if os.path.isfile(filepath):
            if filename in f:
                os.remove(filepath)
        elif os.path.isdir(filepath):
            delete_files_with_filename(filepath, filename)

def delete_all_files(path):
    del_list = os.listdir(path)
    for f in del_list:
        filepath = os.path.join(path, f)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            delete_all_files(filepath)
            os.rmdir(filepath)

if __name__ == '__main__':
    get_argument()
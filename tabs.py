import os
import string
from datetime import datetime
import locale

# set default to german
locale.setlocale(locale.LC_ALL, 'German')

def split_line(line):
    return [s.strip() for s in line.split('\t')]

def readlines(fname):
    with open(fname, 'r') as f:
        for line in f:
            trim_line = line.strip()
            if len(trim_line) < 1 or trim_line.startswith('#'):
                continue
            values = split_line(line)
            yield values

def read_directory(dirname):
    for root, _, files in os.walk(dirname):
        for name in files:
            fname = os.path.join(root, name)
            for line in readlines(fname):
                yield line

# %m/%d/%Y %H:%M
def str2date(date_str, format):
    return datetime.strptime(date_str, format)

# 12.345,83202
def str2float(string):
    return locale.atof(string)

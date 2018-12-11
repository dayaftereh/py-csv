import csv
import os
from datetime import datetime
import locale

# set default to german
locale.setlocale(locale.LC_ALL, 'de_DE')

class CSVWriter:

    def __init__(self, fname, delimiter=' '):
        self._f = None
        self._counter = 0       
        self._writer = None
        self._fname = fname
        self._delimiter = delimiter
        self._open_writer()

    def _open_writer(self):
        fname = self._next_name()
        self._f = open(fname, 'w')
        self._writer = csv.writer(self._f, delimiter=self._delimiter)
    
    def _next_name(self):
        if self._counter < 1:
            self._counter = self._counter + 1
            return self._fname
        parent = os.path.dirname(self._fname)
        fname = os.path.basename(self._fname)
        splittxt = os.path.splitext(fname)
        next_fname = "%s.%d%s" % (splittxt[0], self._counter, splittxt[1])
        next_name = os.path.join(parent, next_fname)
        self._counter = self._counter + 1
        return next_name
        
    def next_file(self):
        if not self._f is None:
            self._f.close()
            self._f = None
        self._open_writer()

    def writerow(self, row):
        self._writer.writerow(row)


def read_directory(dirname, delimiter=' '):
    for root, _, files in os.walk(dirname):
        for fname in files:
            csvfile = os.path.join(root, fname)
            for line in read(csvfile, delimiter):
                yield line

def read(csvfile, delimiter=' '):
    with open(csvfile) as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            yield row

def writer(csvfile, delimiter=' '):
    f = open(csvfile, 'w')
    writer = csv.writer(f, delimiter=delimiter)
    return writer

def str2date(date_str, format):
    return datetime.strptime(date_str, format)

def str2datetime(date, time=None):
    if time is None:
        return datetime.strptime(date, '%m/%d/%Y')
    dateString = '%s %s' % (date, time)
    return datetime.strptime(dateString, '%m/%d/%Y %H:%M')

def str2float(string):
    return locale.atof(string)


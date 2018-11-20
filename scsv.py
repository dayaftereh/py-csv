import csv
from datetime import datetime
import locale

# set default to german
locale.setlocale(locale.LC_ALL, 'de_DE')

def read(csvfile, delimiter=' '):
    with open(csvfile) as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            yield row

def writer(csvfile, delimiter=' '):
    f = open(csvfile, 'w')
    writer = csv.writer(f, delimiter=delimiter)
    return writer

def str2date(date, time=None):
    if time is None:
        return datetime.strptime(date, '%m/%d/%Y')
    dateString = '%s %s' % (date, time)
    return datetime.strptime(dateString, '%m/%d/%Y %H:%M')

def str2float(string):
    return locale.atof(string)


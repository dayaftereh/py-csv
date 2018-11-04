import csv

def read(csvfile, delimiter=' '):
    with open(csvfile, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            yield row

def writer(csvfile, delimiter=' '):
    f = open(csvfile, 'w')
    writer = csv.writer(f, delimiter=delimiter)
    return writer
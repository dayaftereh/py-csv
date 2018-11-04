
import scsv

for line in scsv.read('test.csv', delimiter=';'):
    print(line)

writer = scsv.writer("out.csv")
writer.writerow(["key2", "value1", "value2", "value 3"])
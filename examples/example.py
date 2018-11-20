import scsv

# define the file name for the data
fname = 'data.csv'

# define a new dict to store found keys
map = {}
# read the csv line by line
for line in scsv.read(fname, delimiter=','):
    # get the lines for key or an empty list
    lines = map.get(line[0], [])
    # add line to the lines with same key
    lines.append(line)
    # set the lines for the key
    map[line[0]] = lines

# get all keys and lines
for k, lines in map.items():
    # check if a key is dopple
    if len(lines) > 1:

        # sort the lines after the date
        lines.sort(key=lambda line: scsv.str2date(line[3], line[4]))

        # print all lines
        for line in lines:        
            # print key and the values
            print(k, scsv.str2float(line[2]), scsv.str2date(line[3]), scsv.str2date(line[3], line[4]))

import csv, sys


def make_piviot(x, y, z):
    d = {}
    y=int(y)
    with open(x, 'rU') as csvfile:
        s = csv.reader(csvfile, dialect='excel', delimiter=",", quotechar='"')
        for row in s:
            if row[y] not in d.keys():
                d[row[y]] = 1
            else:
                d[row[y]] += 1
    # return d
    fo = open(z, "w")
    r = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for item in r:
        fo.write(str(item[0]) + "," + str(item[1])+"\n")
    fo.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(sys.argv) !=4:
        print '''
        Usage:
        python csvpiviot.py infile piviot_from_index outfile

        Example
        python csvpiviot.py piviotme.csv 1 magic.csv
        '''
    else:make_piviot(*args)

__author__ = 'techbk'
import csv

def readcsv(file,iftrain):
    ifile  = open(file, "rt", encoding="utf8")
    reader = csv.reader(ifile)
    #print(reader)
    table = []
    rownum = 0
    colnum = 0
    for row in reader:
        # Save header row.
        if rownum == 0 and iftrain == 1:
            rownum += 1
            continue
        else:
            values = []
            _colnum = 0
            for col in row:
                value = col
                try:
                    value = float(col)
                except ValueError:

                    pass
                finally:
                    values.append(value)
                    #print '%-8s: %s' % (header[colnum], col)
                _colnum += 1
            if rownum == 1:
                colnum = _colnum
            rownum += 1
            table.append(values)
    ifile.close()
    rownum -= 1
    return rownum,colnum,table #rownum = so row - 1, colnum = so col

if __name__ == '__main__':
    #print(readcsv(file='prostate-training-data.csv'))
    xxx = readcsv('prostate-training-data.csv',1)
    #print(xxx[0])
    for row in range(0,xxx[0]):
        print(row)
        print(xxx[2][row])
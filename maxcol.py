__author__ = 'techbk'

from readcsv import readcsv
import math

def column(col,table):
    #for row in range(0,rownum):
    #print(len(table))
    for row in range(0,len(table)):
        #print(row)
        yield math.fabs(table[row][col])

def maxcolumn(colnum,table):
    for col in range(0,colnum-1):
        #print(col)
        yield max([x for x in column(col,table)])

def maxcol(colnum,table):
    return [x for x in maxcolumn(colnum,table)]

def maxall(colnum,test,train):
    testmax = maxcol(colnum,test)
    trainmax = maxcol(colnum,train)
    _maxall = []
    for col in range(0,colnum-1):
        _maxall.append(max(testmax[col],trainmax[col]))
    return _maxall


if __name__ == '__main__':
    rownum,colnum,table = readcsv(file='prostate-training-data.csv')
    #print(x for x in collumn(rownum,colnum,table))
    print(maxcol(rownum,colnum,table))


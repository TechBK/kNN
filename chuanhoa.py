from __future__ import division
__author__ = 'techbk'

from maxcol import maxcol
from readcsv import readcsv


def chuanhoa(colnum,table,maxchuanhoa):
    standardtable = []
    for row in range(0,len(table)):
        values = []
        for col in range(0,colnum-1):
            values.append(table[row][col]/maxchuanhoa[col])
        values.append(table[row][-1])# add gia tri cuoi
        standardtable.append(values)
    return standardtable

if __name__ == '__main__':
    rownum,colnum,table = readcsv(file='prostate-training-data.csv')
    for row in chuanhoa(rownum,colnum,table):
        print(row)
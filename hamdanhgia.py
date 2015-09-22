__author__ = 'techbk'

from math import fabs

def hamsaiso(testtable,listdaura):
    sai_so = 0
    for i in range(0,5):
        sai_so += fabs(testtable[i][-1]-listdaura[i])
        #if testtable[i][-1] == listdaura[i]:
            #soketquadung +=1
    return sai_so/5

def hamdanhgia(testtable,ketquamoi,ketquatoiuu):
        ketquamoi.append(hamsaiso(testtable,ketquamoi[2]))
        if not ketquatoiuu: return ketquamoi
        if ketquatoiuu[-1] > ketquamoi[-1]:
            return ketquamoi
        else:
            return ketquatoiuu


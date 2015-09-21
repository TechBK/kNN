__author__ = 'techbk'

from copy import deepcopy
from hamkhoangcach import hamkhoangcach
from chuanhoa import chuanhoa
from readcsv import readcsv
from maxcol import maxall,maxcol

def tim_tap_nb(z,traintable,w,colnum,k):
    tap_nb = deepcopy(traintable)
    for x in tap_nb:
        #if hamkhoangcach(x,z,w,colnum-1) < d: #truyen vao colnum da~ xac dinh
        d = hamkhoangcach(x,z,w,colnum-1)
        x.append(d)
        print("phan tu x trong nb",x)
        print("khoang cach: ",d)
        #tap_nb.append(y)
    tap_nb.sort(key=lambda y: y[-1]) #y[-1] lay phan tu cuoi cung
    tap_nbk = tap_nb[0:k] #lay k phan tu dau tien
    return tap_nbk


if __name__ == '__main__':
    w = [1,1,1,1,1,1,1,1]
    train = readcsv('prostate-training-data.csv',1)
    print("file train: ",train)
    test = readcsv('prostate-test-Vi-Du.csv',0)
    #print("row cua test:", len(test[2]))
    print("file test:",test)

    colnum = train[1]

    #tim max chuan hoa
    print("colnum :",colnum )
    print("max cua train: ", maxcol(colnum, train[2]))
    print("max cua test: ", maxcol(colnum, test[2]))


    maxchuanhoa = maxall(colnum,test[2],train[2])
    print("max chuan hoa",maxchuanhoa)

    traintable = chuanhoa(colnum,train[2],maxchuanhoa)
    testtable = chuanhoa(colnum,test[2],maxchuanhoa)
    def hamdaura(k):
        for z in testtable:
            print("\n########################")
            print("tap nb cua z = ", z)
            tap_nbk = tim_tap_nb(z,traintable,w,colnum,k)

            #len_tap_nb = len(tap_nb)  len = k
            #if(len_tap_nb == 0): break
            #print("len cua tap nb: ",len_tap_nb)

            #if len_tap_nb == 0:
                #print("ko co dau ra")
                #yield "null"
            #elif len_tap_nb == 1:
                #print(tap_nb)
                #print("dau ra:",tap_nb[colnum-1])
            #else:

            daura = sum(x[-2] for x in tap_nbk)/k
            print("daura :", daura)
            yield daura

    def ketqua():
        #for d in [0.01, 0.015, 0.05, 0.1, 0.15]:
        for k in [1, 2, 3, 4, 5]:
            print('@@@@@@@@@@@@@@@@@@@@@@@')
            print("Voi d =", k)
            listdaura = [daura for daura in hamdaura(k)]
            soketquadung = 0

            #for z,i in testtable,range(0,5):
                #for i in range(0,5):
                if z[-1] == listdaura[i]:
                    soketquadung +=1
            print("\nso ket qua dung:", soketquadung)
            print("\n danh sach dau ra",listdaura)

            yield soketquadung,k,listdaura

    bien = [ket for ket in ketqua()]

    print("\n*****************************\nketquacuoicung:")
    for ket in bien:
        print("\n",ket)







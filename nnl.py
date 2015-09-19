__author__ = 'techbk'

from hamkhoangcach import hamkhoangcach
from chuanhoa import chuanhoa
from readcsv import readcsv
from maxcol import maxall,maxcol

def tim_tap_nb(z,traintable,w,colnum,d):
    tap_nb = []
    for x in traintable:
        if hamkhoangcach(x,z,w,colnum-1) < d:
            print("khoang cach: ",hamkhoangcach(x,z,w,colnum-1))
            print("phan tu k trong nb",x)
            tap_nb.append(x)
    return tap_nb



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
    def hamdaura(d):
        for z in testtable:


                print("\n########################")
                print("tap nb cua z = ", z)
                tap_nb = tim_tap_nb(z,traintable,w,colnum,d)

                len_tap_nb = len(tap_nb)
                #if(len_tap_nb == 0): break
                print("len cua tap nb: ",len_tap_nb)

                if len_tap_nb == 0:
                    print("ko co dau ra")
                    yield "null"
                #elif len_tap_nb == 1:
                    #print(tap_nb)
                    #print("dau ra:",tap_nb[colnum-1])
                else:
                    daura = sum(k[colnum-1] for k in tap_nb)/len_tap_nb
                    print("daura :", daura)
                    yield daura
    def ketqua():
        for d in [0.01, 0.015, 0.05, 0.1, 0.15]:
            print('@@@@@@@@@@@@@@@@@@@@@@@')
            print("Voi d =", d)
            listdaura = [daura for daura in hamdaura(d)]
            soketquadung = 0
            for z in testtable:
                for i in range(0,5):
                    if z[colnum-1] == listdaura[i]:
                        soketquadung +=1
            print("\nso ket qua dung:", soketquadung)
            print("\n danh sach dau ra",listdaura)

            yield soketquadung,d,listdaura

    bien = []
    for ket in ketqua():
        bien.append(ket)

    print("\n*****************************\nketquacuoicung:")
    for ket in bien:
        print("\n",ket)







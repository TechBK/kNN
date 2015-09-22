__author__ = 'techbk'

from copy import deepcopy
from hamkhoangcach import hamkhoangcach,hamtrongso
from chuanhoa import chuanhoa
from readcsv import readcsv
from maxcol import maxall,maxcol
from hamdanhgia import hamdanhgia

def tim_tap_nb(z,traintable,w,colnum,k,alpha):
    tap_nb = deepcopy(traintable)
    for x in tap_nb:
        #if hamkhoangcach(x,z,w,colnum-1) < d: #truyen vao colnum da~ xac dinh
        d = hamkhoangcach(x,z,w,colnum-1)
        v = hamtrongso(alpha, d)
        x.append(d)
        x.append(v)
        #print("phan tu x trong nb",x)
        #print("khoang cach: ",d)
        #tap_nb.append(y)
    tap_nb.sort(key=lambda y: y[-2]) #y[-2] lay phan tu d, v la [-1]
    #print("\ntop tap_nb:", tap_nb[0])
    tap_nbk = tap_nb[0:k] #lay k phan tu dau tien
    return tap_nbk

def ham_w(gioihan):
    for a in range(1,gioihan):
        for b in range(1,gioihan):
            for c in range(1,gioihan):
                for d in range(1,gioihan):
                    for e in range(1,gioihan):
                        for f in range(1,gioihan):
                            for g in range(1,gioihan):
                                for h in range(1,gioihan):
                                    yield [a,b,c,d,e,f,g,h]


if __name__ == '__main__':
    alpha = 0.01
    w = [1,1,1,1,1,1,1,1]
    train = readcsv('prostate-training-data.csv',1)
    #print("file train: ",train)
    test = readcsv('Nguyen-Quang-Binh-test.csv',0)
    #print("row cua test:", len(test[2]))
    #print("file test:",test)

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
            #print("\n########################")
            #print("tap nb cua z = ", z,)
            tap_nbk = tim_tap_nb(z,traintable,w,colnum,k,alpha)

            #print("\ntap nbk: ",tap_nbk)
            tong_v = sum(x[-1] for x in tap_nbk)

            tong_v_f = sum(x[-1]*x[-2] for x in tap_nbk)
            daura = tong_v_f/tong_v
            #daura = sum(x[-2] for x in tap_nbk)/k


            #print("daura :", daura)
            yield daura


    def ketqua():
        ketquatoiuu = []
        for w in ham_w(5):

            #for d in [0.01, 0.015, 0.05, 0.1, 0.15]:
            for k in range(5,10):
                #k = 1
                #print('@@@@@@@@@@@@@@@@@@@@@@@')
                #print("Voi k =", k)
                listdaura = [daura for daura in hamdaura(k)]

                ketquamoi=[]
                ketquamoi.append(k)
                ketquamoi.append(w)
                ketquamoi.append(listdaura)
                ketquatoiuu = hamdanhgia(testtable,ketquamoi,ketquatoiuu)
                print(w)
                print(ketquatoiuu)
        return ketquatoiuu

    #bien = [ket for ket in ketqua()]\
    ket_qua = ketqua()

    print("\n*****************************\nketquacuoicung:")
    print("\nvoi k = ",ket_qua[0]," w =  ",ket_qua[1])
    print("list dau ra\n",ket_qua[2])







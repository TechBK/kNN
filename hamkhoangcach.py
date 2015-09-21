__author__ = 'techbk'

from math import sqrt

def hamkhoangcach(x,z,w,colnum):
    #print("colum trong ham khoang cach", colnum)
    sum_bp = 0
    for col in range(0,colnum):
        xxx = (x[col]-z[col])**2
        #print(xxx)
        sum_bp += w[col]*xxx
        #print(sum_bp)
    sum_bp = sqrt(sum_bp)
    return sum_bp

def hamtrongso(alpha,d):
    return 1/(alpha+d)


if __name__ == '__main__':
    w = [1,1,1,1,1,1,1,1]
    x = [-0.1517450792084531, 0.5793383082485232, 0.6329113924050633, -0.59592201977661, 0.0, -0.5217994746835908, 0.6666666666666666, 0.0]
    #z = [-0.1517450792084531, 0.5793383082485232, 0.6329113924050633, -0.59592201977661, 0.0, -0.5217994746835908, 0.6666666666666666, 0.0]
    z = [-0.2602071013957041, 0.6944267854688632, 0.7341772151898734, -0.59592201977661, 0.0, -0.5217994746835908, 0.6666666666666666, 0.0]
    print(hamkhoangcach(x,z,w,9))
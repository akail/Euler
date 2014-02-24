#!/usr/bin/env python2

import numpy

def vert(data):
    maxv=0
    for i in range(17): # number of rows in column
        for j in range(20): # # of columns
            product =1
            for k in range(4):
                product *= data[i+k][j]
        
            if product > maxv:
                maxv = product

    return maxv

def hori(data):
    maxv=0
    for i in range(17): # number of rows in column
        for j in range(20): # # of columns
            product =1
            for k in range(4):
                product *= data[j][i+k]
        
            if product > maxv:
                maxv = product

    return maxv

def diag(data):
    maxv=0
    for i in range(0,17): # number of rows in column
        for j in range(0,17): # # of columns
            product =1
            for k in range(0,4):
                product *= data[j+k][i+k]
        
            if product > maxv:
                maxv = product

    return maxv

def diag2(data):
    maxv=0
    for i in range(19,2,-1): # column
        for j in range(17): # row
            product =1
            for k in range(0,4):
                product *= data[j+k][i-k]
        
            if product > maxv:
                maxv = product

    return maxv

if __name__ == "__main__":
    data = numpy.loadtxt("data.txt")
    vlist=[]
    vlist.append(vert(data) )
    vlist.append(hori(data) )
    vlist.append(diag(data) )
    vlist.append(diag2(data) )
    vlist.sort()
    print int(vlist[3])



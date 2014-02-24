#!/usr/bin/env python2

import numpy as np

data=np.loadtxt('series.txt',dtype=[('mystring','S50')])

datalist=[]

for i in range(20):
    for j in range(50):
        datalist.append( int( data[i][0][j]))

tcomb=len(datalist)-4

productmax=0
for i in range(tcomb):
    product=1
    for j in range(5):
        product*=datalist[i+j]
    
    if product >= productmax:
        productmax=product

print productmax

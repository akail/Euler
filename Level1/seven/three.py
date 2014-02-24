#!/usr/bin/python2

i,j=2,600851475143

while j>1:
    if(i==j):
        break
    if(j%i==0):
        j=j/i
    else:
        i+=1

print(i)

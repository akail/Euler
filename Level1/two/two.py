#!/usr/bin/python2

#import scipy
#import numpy
#import math

fibmax=4000000
fib1=1
fib2=1 
fib3=0
sum=0

while fib3 < fibmax:
    fib3=fib1+fib2
    if( (fib3 % 2) == 0):
       sum+=fib3

    fib1=fib2
    fib2=fib3


print sum
        


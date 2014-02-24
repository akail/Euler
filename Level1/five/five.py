#!/usr/bin/env python2

import math




# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.


# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

value=20
base=20
increment=1

while True:
   
    modcheck =0
    for i in range(11,20):
        modcheck += value%i
        

    #print modcheck
    if modcheck == 0:
        print value
        break

    increment=increment+1
    value=base*increment
    #print value

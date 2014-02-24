#!/usr/bin/env python2

import time
import random
import math

def factor(n):
      factors = set()
      for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
          factors.add(x)
          factors.add(n//x)
      return len(factors)

tlevel=1
ndiv =0
search= int(raw_input('How many divisors? '))
#search= 6

while ndiv <= search:

    ndiv =0
    tnum=tlevel*(tlevel+1)/2


    ndiv += factor(tnum)

    if ndiv >= search:
        print tnum
        break
    #print tnum
    #print ndiv
    tlevel +=1

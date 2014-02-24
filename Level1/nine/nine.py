#!/usr/bin/env python2

import math
import time

def pythagtrip(n):
    for a in range(1,n-1):
        for b in range(a,n):
            for c in range(b,n+1):
                if (a**2 + b**2) == (c**2):
                    if (a+b+c) == n:
                        return (a*b*c)

if __name__ == "__main__":
    time0= time.clock()
    print pythagtrip(1000)
    time1= time.clock()
    s= 'Runtime is '+ str(time1-time0)
    print s

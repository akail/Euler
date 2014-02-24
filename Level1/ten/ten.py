#!/usr/bin/env python2

import math
import time
import random


def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    if n == 3:
        return True

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def primesum(n):

    pval,sum=3,2
    while pval < n:
        if miller_rabin(pval,40):
            sum +=pval

        pval+=2

    return sum

if __name__ == "__main__":
    time0= time.clock()
    print primesum(2000000)
    time1= time.clock()
    s= 'Runtime is '+ str(time1-time0)
    print s



#!/usr/bin/env python2

import time
import random

def prime(n):
    if n == 0:
        print '0 doesn\'t count bud'
    elif n ==1:
        print '1 doesn\'t count bud'
    elif n ==2:
        return True
    else:
        if (n%2) == 0: # if even
            return False
        else: # check if odd and greater than 2
            fmax = (n-n%2)/2 # max factor
            for i in range(3,fmax):
                if n%i == 0:
                    return False
        
            return True

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


def nthprime(j):
    pcount=2
    number=5
    while pcount <j:
        #if prime(number):
        if miller_rabin(number,30):
            pcount +=1

        number +=2

    return number-2

def nthprimeold(j):
    pcount=2
    number=5
    while pcount <j:
        if prime(number):
            pcount +=1

        number +=2

    return number-2


if __name__ == "__main__":
    time0= time.clock()
    print nthprimeold(10001)
    time1= time.clock()
    s= 'Runtime is '+ str(time1-time0)
    print s

    time0= time.clock()
    print nthprime(10001)
    time1= time.clock()
    s= 'Runtime is '+ str(time1-time0)
    print s

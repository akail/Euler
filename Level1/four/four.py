#!/usr/bin/env python2

import numpy
import scipy
import math



# Determine if a number is a palindrome
#find palindrome of product of two 3 digit numbers
stack=[2]

for i in range(999,100,-1):

    for j in range(999,100,-1):

        pcheck = i*j
        pstring = str(pcheck)
        plength = len(pstring)

        for k in range(plength - (plength % 2)):

            if pstring[k] != pstring[-k-1]:
                palindrome =  False
                break

            else:
                palindrome = True
    
        if palindrome == True:
            stack.append(pcheck)

           
stack.sort()
stack.reverse()
print stack[0]

            




#!/usr/bin/env python2
import math

sumsquare=0
squaresum=0

for i in range(101):
    sumsquare += i**2
    squaresum += i

print squaresum**2 - sumsquare

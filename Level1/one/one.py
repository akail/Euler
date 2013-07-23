#!/usr/bin/python

import scipy
import numpy
import math

counter = 0
sum = 0
range = 100

while counter < range:
    if ((counter % 3) == 0) or ((counter %5) == 0):
        sum +=counter

    counter +=1

print sum


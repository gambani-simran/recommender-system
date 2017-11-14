# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy
arr = raw_input().strip().split(' ')
a = numpy.array(arr,dtype=int)
print numpy.reshape(a,(3,3))


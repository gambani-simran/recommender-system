# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy
arr = raw_input().strip().split(' ')

a = numpy.array(arr,dtype=float)
print numpy.floor(a)
print numpy.ceil(a)
print numpy.rint(a)

# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy
arr = tuple(map(int,raw_input().strip().split(' ')))

print numpy.zeros(arr, dtype = numpy.int)

print numpy.ones(arr, dtype = numpy.int)

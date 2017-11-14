# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])

a1 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])
print numpy.max(numpy.min(a1,axis=1))

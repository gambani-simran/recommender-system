# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])

a1 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])

print numpy.prod(numpy.sum(a1,axis=0))

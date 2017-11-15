# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])
a1 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])
print numpy.mean(a1,axis=1)
print numpy.var(a1,axis=0)
print numpy.std(a1,axis=None)

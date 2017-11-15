# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy
n = int(raw_input())

a1 = numpy.array([list(map(float,raw_input().split(' '))) for i in range(0,n)])

print numpy.linalg.det(a1)

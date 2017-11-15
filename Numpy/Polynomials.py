# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy
arr = list(map(float,raw_input().strip().split(' ')))
n = int(raw_input())

print numpy.polyval(arr,n)

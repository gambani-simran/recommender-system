# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])

a1 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])
a2 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])

print numpy.add(a1,a2)
print numpy.subtract(a1,a2)
print numpy.multiply(a1,a2)
print numpy.divide(a1,a2)
print numpy.mod(a1,a2)
print numpy.power(a1,a2)

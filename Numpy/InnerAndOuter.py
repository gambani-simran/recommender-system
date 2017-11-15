# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy
import numpy
a1 = map(int,raw_input().strip().split(' '))
a2 = map(int,raw_input().strip().split(' '))

a = numpy.array(a1)
b = numpy.array(a2)

print numpy.inner(a,b)
print numpy.outer(a,b)

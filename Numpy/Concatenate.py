# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])
p = int(arr[2])
a1 = numpy.array( [list(map(int, raw_input().split())) for i in range(n)] )
a2 = numpy.array( [list(map(int, raw_input().split())) for i in range(m)] )

print numpy.concatenate((a1, a2), axis = 0)

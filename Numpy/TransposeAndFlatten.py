# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])
a =[]
for i in range(0,n):
    a.append(raw_input().strip().split(' '))
arr = numpy.array(a,dtype=int)
print arr.transpose()
print arr.flatten()

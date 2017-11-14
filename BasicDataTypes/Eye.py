# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy
arr = raw_input().strip().split(' ')
n = int(arr[0])
m = int(arr[1])
print numpy.eye(n,m,k=0)

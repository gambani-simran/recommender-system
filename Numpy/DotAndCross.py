# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy
n = int(raw_input())
a1=[]
a2 = []
#a1 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])
for i in range(0,n):
    x = list(map(int,raw_input().split(' ')))
    a1.append(x)
a = numpy.array(a1)

for i in range(0,n):
    y = list(map(int,raw_input().split(' ')))
    a2.append(y)
b = numpy.array(a2)
#a2 = numpy.array([list(map(int,raw_input().split(' '))) for i in range(0,n)])

print numpy.dot(a,b)

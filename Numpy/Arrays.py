# https://www.hackerrank.com/challenges/np-arrays/problem

def arrays(arr):
    # complete this function
    # use numpy.array 
    a = numpy.array(arr, dtype=float)
    return numpy.flipud(a) #flip upside down



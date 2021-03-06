# Dot and Cross

# ========== Dot ========== 
# The dot tool returns the dot product of two arrays.
''' import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.dot(A, B))       #Output : 11    '''
# ========== Cross ========== 
# The cross tool returns the cross product of two arrays.
''' import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print(numpy.cross(A, B))     #Output : -2    ''' 

# Task: You are given two arrays A and B. Both have dimensions of NxN. 
# Your task is to compute their matrix product.
# Sample Input
''' 2
    1 2
    3 4
    1 2
    3 4 '''
# Sample Output
''' [[ 7 10]
     [15 22]]   '''


import numpy as np

n = int(input())
A = np.array([input().split() for _ in range(n)], int)
B = np.array([input().split() for _ in range(n)], int)
print(np.dot(A,B))
"""
Docstring for Numpy.Numpy.2
"""

"""
    Array Creation Functions (Very Important)
"""
import numpy as np

"""
    Zero Arrays [
        [0,0],
        [0,0]
    ]
"""

zero_arr = np.zeros((3,3) , dtype=int)
print(zero_arr)

print("\n")

"""Ones matrix mean all elements are 1's"""

one_arr = np.ones((2,4) , dtype=int)
print(one_arr)

"""Matrix with same element which you want like 7"""

full_arr = np.full((2,2) , 7)
print(full_arr)

"""matrix with proper interval (start , end(exculde) , interval)"""
arange_arr = np.arange(0 , 10 , 2)
arange_arr2 = np.arange(0,10,3)
print(arange_arr)
print(arange_arr2)


"""if you want a array bw two number how many you want 5 elements b/w 0 to 1"""
linspace_arr = np.linspace(0,1,5)
print(linspace_arr)


"""identity matrix"""

print(np.eye(3))
print(np.random.rand(3))
print(np.random.randn(3))
print(np.random.randint(1,10,(2,3)))


"""Data Types & Memory Control"""

"""
    In numpy , we use dtype like int32 , int64 , float32 , float64 , bool

    float32 uses half memory
    GPUs prefer float32
    Large datasets depend on this
"""

"""Indexing, Slicing & Views"""

index_arr = np.array([10,20,30,40,50])

print(f"Indexinng\n{index_arr[1]}\n{index_arr[-1]}\n")

print(f"slicing\n{index_arr[1:3]}")

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m[0, 1]) #0th's rows 1's element
print(m[:, 1])
print(m[1, :])


"""copy of array"""

copy = m.copy()
print(copy)

"""Boolean indexing"""

bool_indexing = np.array([10,20,30,40,50])

print(bool_indexing[bool_indexing > 25])

print(bool_indexing[(bool_indexing > 25) & (bool_indexing < 40)])

"""Vectorization (MOST IMPORTANT)"""

"""
in python we used 
    result = []
    for x in a:
        result.append(x * 2)

"""

"""in numpy we use insted of these"""

print(bool_indexing*2) #output [ 20  40  60  80 100]

"""
    Broadcasting (Advanced Concept)
"""

a = np.array([1, 2, 3])
b = 10
print(a + b)

m = np.array([[1, 2, 3],
              [4, 5, 6]])
o = m + np.array([10, 20, 30])

print(o)



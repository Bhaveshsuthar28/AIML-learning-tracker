import numpy as np

numpy_array_1D = np.array([1,2,3])

numpy_array_2D = np.array([
    [1,2,4],
    [2,3,4]
])

print(numpy_array_2D)
print(numpy_array_1D)

"""dimensions of array"""

print(numpy_array_2D.ndim) #output 2
print(numpy_array_1D.ndim) #output 1


"""size per dimension"""

print(numpy_array_2D.shape)  #output (rows , columns)
print(numpy_array_1D.shape)  #output (rows , columns)

"""datatype"""

print(numpy_array_2D.dtype)

"""total elements"""

print(numpy_array_2D.size)

"""bytes per elements"""

print(numpy_array_2D.itemsize)
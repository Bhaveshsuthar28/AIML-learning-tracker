import numpy as np


arr = np.array([1,2,3,4,5,6])

arr2 = arr.reshape(2,3)

print(arr)
print(arr2)

new_arr = np.insert(arr2 , 1 , 8 , axis=0)
new_arr2 = np.insert(arr2 , 1 , 8 , axis=1)
print(new_arr)
print(new_arr2)


"""
    np.concatenate((arr1 , arr2) , axis=0&1)

    axis 0 > vertical stacking
    axis 1 > horizontal stacking

"""

first = np.array([1,2,3])
second = np.array([5,6,7])

third = np.concatenate((first , second) , axis=0)
print(third)
"""Handling Missing Value"""

import numpy as np

"""
    np.isnan ->>> its detect missing value

    np.nan_to_num ->> if you want to fill missing value from someone so we use np.nan_to_num

    np.isinf() --> its detect infinte number
"""

arr = np.array([1,2,3,np.nan , 4 , np.nan] , dtype=float)

print(np.isnan(arr))

Clear = np.nan_to_num(arr , 100)
print(Clear)
"""we can't compare directly 
    np.nan == np.nan
"""

a = np.random.rand(3,4)
b = np.random.rand(4,2)

c = a @ b

print(c)
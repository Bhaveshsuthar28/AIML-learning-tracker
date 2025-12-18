'''lambda arguments : expression'''
from functools import reduce

Add = lambda a , b : a + b

print(Add(5 , 6))

max_value = lambda a,b : a if a > b else b

print(max_value(7,6))

nums = [1,2,3,4,5]

sq = list(map(lambda x : x**2 , nums))

print(sq)

even = list(filter(lambda x : x%2 == 0 , nums))

print(even)

total = reduce(lambda a,b : a+b , nums)

print(total)
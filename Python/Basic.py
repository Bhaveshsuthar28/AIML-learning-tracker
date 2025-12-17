# def update(x):
#     x += 1

# a = 10
# update(a)


name = "Bhavesh"

a = "5"

b = int(a)
print(b)
print(type(b))

def printNumber(a , b):
    return a+b

f = printNumber

print(f(5,7))

def add(a : int , b : int) -> int:
    """return sum of a and b"""

    return a+b


a = 5
b = 6

print(add(a,b))
print(add.__doc__)


#List

lst = [10, 20 , 20]

print(lst[::-1])


#Tuple 

"""no add and remove in tuple"""

dit = {
    "age" : 20,
    "salary" : 4000
}

print(dit["age"])


#decorators


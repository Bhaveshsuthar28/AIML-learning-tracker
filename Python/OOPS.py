# class Car:
#     def start(self):
#         print("car")


# myCar = Car()

# myCar.start()


class Laptop:
    def power_on(self):
        print("Laptop ON")


myLaptop = Laptop()

myLaptop.power_on()


class Students:

    def __init__(self , roll_no , name):
        self.name = name
        self.roll_no = roll_no

    def info(self):
        print(f"Name : {self.name}\nRoll no. {self.roll_no}")
        

s1 = Students("Bhavesh" , 101)
s2 = Students("Aman" , 102)

s1.info()
s2.info()


try:
    a = int(input("Enter number : "))
    b = 10/a
    print(b)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Division by zero")
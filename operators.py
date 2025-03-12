# Assignment operators
# =, +=, -=, *=, /=, %=, //=, **=
# cars = 10

# cars = cars + 5
# cars =+ 5
# cars -= 5
# cars /= 5
# cars //= 2
# cars *= 5
# cars **= 5
# remainder = cars % 3

# print(cars)

a = 3.14
b = 4
c = 5

# result = round(a)
# result = abs(b)
# result = pow(3, 3)
# result = max(a, b, c)
# result = min(a, b, c)
# result = sum([a, b, c])

# print(result)

# math module
import math

# print(math.pi)
# print(math.e)

# result = math.sqrt(16)
# result = math.ceil(3.14)
# result = math.floor(3.14)
# print(result)

# exercise 1
# create a program that calculates the circumference of a circle
# formula: 2 * pi * r
# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius

# print(f"The circumference of the circle is {round(circumference)} cm")

# exercise 2
# create a program that calculates the area of a circle
# formula: pi * r^2
# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * math.pow(radius, 2)
# print(f"The area of the circle is {round(area, 2)} cm^2")

# exercise 3
# create a program that calculates the volume of a sphere
# formula: 4/3 * pi * r^3
radius = float(input("Enter the radius of the sphere: "))
volume = 4/3 * math.pi * math.pow(radius, 3)
print(f"The volume of the sphere is {round(volume, 2)} cm^3")

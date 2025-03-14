# variables are containers for storing data values
# variables are created when you assign a value to it
# variables are case-sensitive
# variables can be of any type
# variables can be reassigned
# Variables behaves as if it were the value it contains

# variable assignment
# variable_name = value

# name, age = "Cliff", 36
name = "Cliff"
age = 36
pi = 3.14
numbers = [1, 2, 3, 4, 5]
is_active = True

print(name)
print(age)
print(pi)
print(numbers)

# datatypes
print(type(name))
print(type(age))
print(type(pi))
print(type(numbers))
print(type(is_active))

name = input("Press Enter to your name : ")
# print("Hello", name)

print("%s is %d years old" % ("Cliff", age))
print(f"Cliff is {age} years old")
print("Cliff is " + str(age) + "years old")
print("Cliff is ", str(age), "years old")
print("Cliff is {} years old".format(age))

print("%s is %d years old" % (name, age))
print(f"{name} is {age} years old")
print(name + " is " + str(age) + " years old")
print(name, "is", str(age), "years old")
print("{} is {} years old".format(name, age))
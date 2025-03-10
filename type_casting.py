# Typecasting is the process of converting one data type to another data type.
# In this snippet, we will convert the data types of variables to other data types.

name = "John"
quantity = 2
price = 2.99
is_active = True

print(type(name))
print(type(quantity))
print(type(price))
print(type(is_active))

name = bool(name)
quantity = str(quantity)
price = int(price)
is_active = str(is_active)

print(type(name))
print(type(quantity))
print(type(price))
print(type(is_active))

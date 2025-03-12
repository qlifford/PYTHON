

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
# first_number = int(first_number)
# second_number = int(second_number)


if first_number == 0 or second_number == 0:
    print("Cannot divide by zero")
elif first_number + second_number:
    result = first_number + second_number
    print(result)
elif first_number - second_number:
    result = first_number - second_number
    print(result)
elif first_number / second_number:
    result = first_number / second_number
    print(result)
elif first_number * second_number:
    result = first_number * second_number
    print(result)
    # pass
else:
    print("Invalid input")



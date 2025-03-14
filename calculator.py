

first_number = float(input("Enter first number: "))
operator = input("Enter an operator (+ - * /): ")
second_number = float(input("Enter second number: "))
empty = " "
# first_number = int(first_number)
# second_number = int(second_number)

if first_number == 0 or second_number == 0:
    print("Cannot divide by zero")
elif operator == "-":
    result = first_number - second_number
    print(round(result))
elif empty:
    print("You didn't enter anything!")
else:
    print("Invalid input")



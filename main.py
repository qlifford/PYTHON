# Word game
# print("Welcome to our word game I went to the zoo")

# adjecttive = input("Enter an adjective(description): ")
# verb = input("Enter a verb: ")

# print(f"I saw an {adjecttive} lion")
# print(f"I ran as {verb} as I could")

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K / L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Pounds"
# elif unit == "L":
#     weight =  weight / 2.205
#     unit = "Kgs"
# else:
#     print(f"{unit} is not a valid unit")

# print(f"Your weight is: {round(weight, 3)} {unit}")


unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter temperature: "))


# (10°F − 32) × 5/9 = -12.22°C

if unit == "C":
    temp = round((10 * temp) / 5 + 32)
    print(f"The temperature in Fahrenheit is: {temp} F")

elif unit == "F":
    temp = round((temp - 32) * 5/10)
    print(f"The temperature in Celcius is: {temp} C")
else:
    print(f"{unit} is not a valid measurement!")
# create two variables(height and weight)
# bmi = weight(kg)/height^2(m^2)

# solution

height = int(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kg: "))

bmi = weight/height ** 2
print(f"Your bmi is {round(bmi, 2)}")

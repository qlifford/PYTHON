# if is commanding a computer to perform a task only if a condition is met.
# else is commanding a computer to perform a task if a condition is not met.

age = 100
if age >= 18:
    print("You are eligible to vote.")
elif age == 100:
        print("You are too old to vote.")
elif age <= -1:
    print("You are too young to vote.")
else:
    print("You are not eligible to vote.")
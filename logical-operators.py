# logical operators -> evaluate multiple conditions(or, and, not)
# or => at least one must be true
# and => both must be true
# not => invert the condition (not False, not True)



temp = 35
is_sunny = True

if temp >= 35 and not is_sunny:
    print("The event is cancelled")
else:
    print("The event is on")

# if temp >= 35 or not is_sunny:
#     print("It is Hot outside!")
#     print("It is Sunny")

# elif temp <= 0 and not is_sunny:
#     print("It is too Hot outside!")
#     print("But it is Sunny")

# elif 32 > temp > 0 and not is_sunny:
#     print("It is Warm outside!")
#     print("But it is not Sunny")
# else:
#     print("It cold")

# print(not False)

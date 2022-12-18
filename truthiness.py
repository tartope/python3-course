# In python things that are naturally false: empty objects, empty strings, None, and zero.

# animal = input("enter your favorite animal")

# if animal:
#     print(animal + " is my favorite too!")
# else:
# 	print("YOU DIDNT SAY ANYTHING!")
#_____________________________________

# Logical and, or, not:

# and: both sides have to be true
# age = 6

# if age > 2 and age < 8:
#     print("You pay child price")

# or: only one side has to be true
# city = input("Where do you live?")

# if city == "los angeles" or city == "san francisco":
#     print("YOU LIVE IN CALIFORNIA!")
# else:
#     print("YOU LIVE SOMEWHERE ELSE")

# not: truthy if the opposite is true
# age = 21
# age = 7
age = 78

# if age is not between 2-8 AND not 65 or greater (the not operator negates the 'or')
if not((age >= 2 and age <= 8) or age >= 65):
    print("You pay 10 dollars and are not a child or senior.")
else:
    print("You are a child or senior.")

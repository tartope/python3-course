print("How many kilometers did you run today?")
# input() is a function that awaits a users input, and it gives us a string so we have to turn it into a float
kms = input()
# float turns kms (the input) into a decimal
miles = float(kms) / 1.60934
# print("Okay, you said " + miles)        # //=> TypeError: can only concatenate str (not "float") to str
# print(f"That is equal to {miles} miles.")   # //=> "That is equal to 4.970981893198454 miles."

# round(thing to round, how many decimal points)
# print(f"That is equal to {round(miles, 2)} miles.")   # //=> "That is equal to 4.97 miles."

# another option:
miles = round(miles, 2)
# print(f"That is equal to {miles} miles.")   # //=> "That is equal to 4.97 miles."
print(f"Your {kms}km run was {miles}mi.")

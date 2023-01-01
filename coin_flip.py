from random import random

# def flip_coin():
#     #genterate random number 0-1 and save it to variable
#     r = random()
#     #if r is greater than 0.5, return Heads, else return Tails
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# print(flip_coin())

# slightly refactored version
def flip_coin():
    #genterate random number 0-1; if random is greater than 0.5, return Heads, else return Tails
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())
# See modules.py file that defines custom modules
# this file refers to apples.py and bananas.py

# import bananas
# import apples

# print(bananas.dip_in_chocolate())  #//=> Here's a delicious banana, dipped in chocolate!
# print(apples.offer())  #//=> Hey do you like apples?


from bananas import dip_in_chocolate as dip
import apples

print(dip())  #//=> Here's a delicious banana, dipped in chocolate!
print(apples.offer())  #//=> Hey do you like apples?
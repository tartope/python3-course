# my solution:
# for num in range(1, 21):
#     if num % 2 == 0 and num != 4:
#         print(f"{num} is even")
#     elif num % 2 !=0 and num != 13:
#         print(f"{num} is odd")
#     else:
#         print(f"{num} is unlucky")


# course instructor's solution:
# for num in range(1, 21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# course instructor's refactored solution:
for num in range(1, 21):
    if num == 4 or num == 13:
        state = "unlucky"
    elif num % 2 == 0:
        state = "even"  
    else:
        state = "odd"
    print(f"{num} is {state}")
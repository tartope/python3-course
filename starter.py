import random

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!


# version 1:
# ranges are exclusive (does not include 10) but randint is inclusive (does include 10)
# random_number = random.randint(1,10)  # numbers 1 - 10
# guess = None

# while guess != random_number:
#     # this returns a string so if/else statement won't work because "<" or ">" operators are not supported between a string and integer
#     guess = input("Pick a number from 1 to 10: ")
#     # converts guess to integer
#     guess = int(guess)
#     if guess < random_number:
#         print("You guessed too low")
#     elif guess > random_number:
#         print("You guessed too high")
#     else:
#         print("You won!")


# version 2:
# ranges are exclusive (does not include 10) but randint is inclusive (does include 10)
random_number = random.randint(1,10)  # numbers 1 - 10

# while true keeps going forever until it gets to the "break"
while True:
    # this returns a string so if/else statement won't work because "<" or ">" operators are not supported between a string and integer
    guess = input("Pick a number from 1 to 10: ")
    # converts guess to integer
    guess = int(guess)
    if guess < random_number:
        print("You guessed too low")
    elif guess > random_number:
        print("You guessed too high")
    else:
        print("You won!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing.")
            break
import random   # or "from random import randint"
# version one:

print("Rock...")
print("Paper...")
print("Scissors...")

# player1 = input("Player 1, make your move: ")
# player2 = input("Player 2, make your move: ")

# if player1 == "rock" and player2 == "scissors":
#     print("player1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("player2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("player1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("player2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("player2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("player1 wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("something went wrong")

#________________________________________________________________

# version two (refactored):

# player1 = input("Player 1, make your move: ")
# print("***NO CHEATING!!\n\n" * 20)
# player2 = input("Player 2, make your move: ")

# this outer if/else will run if player2 enters something other than rock, paper, or scissors
# if player2 == "rock" or player2 == "paper" or player2 == "scissors":
#     if player1 == player2:
#         print("It's a tie!")
#     elif player1 == "rock":
#         if player2 == "scissors":
#             print("player1 wins!")
#         elif player2 == "paper":
#             print("player2 wins!")
#     elif player1 == "paper":
#         if player2 == "rock":
#             print("player1 wins!")
#         elif player2 == "scissors":
#             print("player2 wins!")
#     elif player1 == "scissors":
#         if player2 == "paper":
#             print("player1 wins!")
#         elif player2 == "rock":
#             print("player2 wins!")
#     else:
#         print("something went wrong")
# else:
#     print("player2 your entry was invalid")

#________________________________________________________________

# version three (random) use "import random" (see line 1) to use this function

# .lower(): changes all the input to lower case
player = input("Player, make your move: ").lower()

rand_num = random.randint(0, 2)     # or rand_num = randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}.")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    elif computer == "rock":
        print("computer wins!")
else:
    print("Please enter a valid move")

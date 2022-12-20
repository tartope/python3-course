message = input("Hey how's it going? ")

while message != "stop copying me":
    print(message)
    message = input()
print("UGH FINE YOU WIN")


# refactored version:
# while message != "stop copying me":
#     message = input(f"{message}\n")
# print("UGH FINE YOU WIN")
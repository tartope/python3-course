# break is a controlled way of exiting a loop.  it breaks immediately so if it's at the beginning, the loop will never begin.

# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break

times = int(input("How many times do I have to tell you? "))

# starts the range from 1 to >=3
for time in range(1, times):
	print("CLEAN UP YOUR ROOM!")
	if time >= 3: 
		print("do you even listen anymore?")
		break
		
import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

# this instance will be pickled
blue = Cat("Blue", "Scottish Fold", "String")
buddy = Cat("Buddy", "American Short Hair", "Treat ball")


# To pickle an object:
# wb means writing binary (it's converted to byte stream when pickle is called)
# with open("pets.pickle", "wb") as file:
# 	# pass in the instance of blue, and the file it gets put in
# 	# pickle.dump(blue, file)  #<-- to pickle one item, or see below
# 	pickle.dump((blue, buddy), file)  #<-- can pickle more than one item in a tuple, or see above

# To unpickle something (bring blue and buddy back to life):
# rb means reading binary
# with open("pets.pickle", "rb") as file:
# 	zombie_blue, zombie_buddy = pickle.load(file)
# 	print(zombie_blue, zombie_buddy)
# 	print(zombie_blue.play(), zombie_buddy.play())


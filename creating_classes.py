# Convention to name classes in singular and use upper camel case:

# class User:
#     # pass allows the code to move on, even though nothing is inside; so no error is returned
#     pass

# # creating an instance of this class (creates a new user); no need to explicitly call _init_() when creating an instance because Python knows to do it
# user1 = User()
# print(user1)  #//=> <__main__.User object at 0x10223c450>  (a user object was created; the alphanumeric string is the location in memory)
# print(type(user1)) #//=> <class '__main__.User'> (shows us its a class User)


# when creating classes, almost always need an __init__ method (must be double underscore), and pass "self" as a parameter
class User:
    # the "self" keyword refers to the specific instance of the User class

    active_users = 0            # <-- class attribute

    def __init__(self, first, last, age):
        # print("A new uswer has been made!")
        # think of like self.variable_name = parameter, or self.key(in dictionary): value (parameter)
        self.first = first      # <-- instance attribute
        self.last = last        # <-- instance attribute
        self.age = age          # <-- instance attribute
        # anytime a new user is initialized, add one to active_users
        User.active_users += 1  # <-- refers to the class attribute/variable

    def logout(self):
        User.active_users -= 1 
        return f"{self.first} has logged out."

    # instance methods:
    # below are getters (they get information but never change anything)
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}."

    def is_senior(self):
        return self.age >= 65

    # setters
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}!"

# user1 = User() #//=> A new uswer has been made!
# user2 = User() #//=> A new uswer has been made!
# user3 = User() #//=> A new uswer has been made!

# user1 = User("Joe", "Smith", 68)
# print(user1.first, user1.last, user1.age) #//=> Joe Smith 68
# user2 = User("Blanca", "Lopez", 41)
# print(user2.first, user2.last) #//=> Blanca Lopez
# print(user2.full_name())  #//=> Blanca Lopez
# print(user1.initials())  #//=> J.S.
# print(user1.likes("Ice Cream"))  #//=> Joe likes Ice Cream.
# print(user2.likes("Chips"))  #//=> Joe likes Chips.
# print(user2.is_senior())  #//=> False
# print(user1.age)  #//=>  68
# print(user1.birthday())  #//=>  Happy 69th, Joe!
# print(user1.age)  #//=>  69

# Referring to class attribute:
# print(User.active_users) #//=> 0
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.active_users) #//=> 2
# print(user2.logout()) #//=>  Blanca has logged out.
# print(User.active_users) #//=> 1
#_____________________________________________________________

# Practice example 1.
# Your First Class - Social Media Comments
# It's time to define your own class! Suppose we're creating a social network application where users can comment on posts and photos.
# Create a class called Comment .  Each comment should have the following attributes:
# username  - the username of the person who created the comment (like "bluethecat")
# text  - the actual comment itself (like "omg so cute!" or "hahah")
# likes  - the number of likes the comment has.  Likes should default to 0.
# The following code should work:
# c = Comment("davey123", "lol you're so silly", 3) 
# c. username       #"davey123"
# c. text           #"lol you're so silly"
# c.likes           #3
# another_comment = Comment("rosa77", "soooo cute!!!") 
# another_comment.username        #"rosa77"
# another_comment.text            #"soooo cute!!!"
# another_comment.likes           #0 
# Hints:
# __init__ is like any other function.  To add a default value for a parameter, just use the equals sign =.  Remember that your default parameters need to come at the end!
class Comment():
    def __init__(self, username, text, likes= 0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("davey123", "lol you're so silly", 3)
# print(c.username, c.text, c.likes)  #//=> davey123 lol you're so silly 3
another_comment = Comment("rosa77", "soooo cute!!!")  
# print(another_comment.username, another_comment.text, another_comment.likes)  #//=> rosa77 soooo cute!!! 0
#_____________________________________________________________

# Underscores: Dunder Methods, Name Mangling and More:

# _name (a single underscore is just convention; it's a way of telling devs that this is supposed to be a private property/method)
# __name (two underscores before the name of an attribute/method is not conventional, it does something behind the scenes; it does something called Name Mangling; its purpose is to make this method/attribute particular to the class that it's in)
# __name__ (a dunder method: a convention that should be respected; you can define your own but you shouldn't; it's used for Python specific methods)
class Person:
    def __init__(self):      #<-- a dunder method
        self.name = "Tony"
        self._secret = "hi"
        self.__msg = "I like turtles!"
        self.__lol = "HAHAHAHA"

p = Person()
# print(p.name)  #//=> Tony
# print(p._secret)  #//=> hi

# print(p.__msg)  #//=> AttributeError: 'Person' object has no attribute '__msg'

# Name Mangling: the combination of the class name and attribute (seen in the beginning of the below print statement):
# print(dir(p))  #//=> ['_Person__lol', '_Person__msg', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_secret', 'name']

# Below is how they are accessed
# print(p._Person__msg)  #//=> I like turtles!
# print(p._Person__lol)  #//=> HAHAHAHA
#_____________________________________________________________

# Practice exercise 2.
# Bank Account OOP Exercise
# Define a new class called BankAccount.  
# Each BankAccount should have an owner , specified when a new BankAccount is created like BankAccount("Charlie") 
# Each BankAccount should have a balance attribute  that always starts out as 0.0 
# Each instance should have a deposit method that accepts a number and adds it to the balance. It should return the new balance.
# Each instance should have a withdraw method that accepts a number and subtracts it from the balance. It should return the new balance.
# acct = BankAccount("Darcy")
# acct.owner #Darcy
# acct.balance #0.0
# acct.deposit(10)  #10.0
# acct.withdraw(3)  #7.0
# acct.balance .  #7.0
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        
    def get_balance(self):
        return self.balance
        
    def deposit(self, num):
        self.balance += num
        return self.balance
        
    def withdraw(self, num):
        self.balance -= num
        return self.balance

acct = BankAccount("Darcy")
# print(acct.owner) #//=>  Darcy
# print(acct.get_balance()) #//=>  0.0
# print(acct.deposit(10)) #//=>  10.0
# print(acct.withdraw(3)) #//=>  7.0
# print(acct.get_balance()) #//=>  7.0
#_____________________________________________________________

# Class Attributes Continued: 
# Another class with a class attribute, used for validation purposes
class Pet:
    # this class attribute stores a list of permitted species
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
# print(cat.species)
# # print(cat.set_species("tiger")) #//=>  ValueError: You can't have a tiger pet!
# cat.set_species("rat")
# print(cat.species) #//=> rat
# # print(Pet.allowed)  #//=> ['cat', 'dog', 'fish', 'rat']
# Pet.allowed.append("pig")  
# # print(Pet.allowed)  #//=> ['cat', 'dog', 'fish', 'rat', 'pig']
# cat.set_species("pig") 
# print(cat.species) #//=> pig
#_____________________________________________________________

# Practice example 3.
# Chicken Coop Exercise
# Suppose we have a big ol chicken coop in our backyard full of very productive hens. We're going to model our chickens with python! We want to keep track of how many eggs each individual Chicken lays, and at the same time we want to track the total number of eggs all hens have laid. 
#  Create a Chicken  class.  Each Chicken has a species  and a name , as well as an integer attribute called eggs . eggs should always start out at 0. 
# Each Chicken should also have an instance method called lay_egg() which should increment and then return that particular Chicken's eggs  attribute. lay_egg()  should also increment a class variable called total_eggs
# c1 = Chicken(name="Alice", species="Partridge Silkie")
# c2 = Chicken(name="Amelia", species="Speckled Sussex")
# Chicken.total_eggs #0
# c1.lay_egg()  #1
# Chicken.total_eggs #1
# c2.lay_egg()  #1
# c2.lay_egg()  #2
# Chicken.total_eggs #3
class Chicken:
    
    total_eggs = 0
    
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0
        
    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs

c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
# print(Chicken.total_eggs) #//=> 0
# print(c1.lay_egg())  #//=> 1
# print(Chicken.total_eggs) #//=> 1
# print(c2.lay_egg())  #//=> 1
# print(c2.lay_egg())  #//=> 2
# print(Chicken.total_eggs) #//=> 3
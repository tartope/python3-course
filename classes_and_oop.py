from copy import copy

# Inheritance

# Parent/base class
# class Animal:
#     # class attribute
#     cool = True

#     # instance method
#     def make_sound(self, sound):
#         print(f"this animal says {sound}")

# # child class; it inherits from Animal because of the "Animal" parameter passed into the Cat class
# class Cat(Animal):
#     # when the method is empty, add "pass" so you don't get an error
#     pass

# a = Animal()
# a.make_sound("chirp")  #//=> this animal says chirp

# blue = Cat()
# even though Cat class is empty, it inherits from the Animal class, and can print "this animal says meow"
# blue.make_sound("meow") #//=> this animal says meow
# # the Cat class inherits from the Animal class, and returns True
# print(blue.cool)  #//=> True
# print(Cat.cool)  #//=> True
# print(Animal.cool)  #//=> True

# can use this to verify that blue is a Cat and also an Animal
# print(isinstance(blue, Cat))  #//=>  True
# print(isinstance(blue, Animal))  #//=>  True
# print(isinstance(blue, object))  #//=>  True
#_______________________________________________________________

# Properties

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        # ._age is for private use
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # getter method:
    # def get_age(self):
    #     return self._age

    # setter method:
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self.age = 0


    # these getter/setter methods use property decorator and are better:
    # use this decorator as a getter to get age
    @property
    def age(self):
        return self._age

    # use this as a setter to set age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0
            # or
            # raise ValueError("age can't be negative!")

    # use this decorator as a getter to get full name
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # use this as a setter to set full name
    @full_name.setter
    def full_name(self, name):
        # assigns the name to first and last based on the space in the split, as compared to the argument
        self.first, self.last = name.split(" ")



jane = Human("Jane", "Goodall", -9)
# print(jane.age)  #//=> 0
# the problem with above line is someone can change age with line below:
# jane.age = -100  #<-- problematic and one fix can be with if statement for age in __init__ method

# after changing "age" to "_age" in __init__ method
# print(jane.age)  #//=> 'Human' object has no attribute 'age'. Did you mean: '_age'?

# after writing get_age and set_age
# print(jane.get_age())  #//=> 0
# jane.set_age(45)  
# print(jane.get_age()) #//=> 45

# after using property:
# even though it's a method, no parentheses needed
# print(jane.age)  #//=> 0
# jane.age = 20
# print(jane.age)  #//=> 20
# jane.age = -100
# print(jane.age)  #//=> 0

# # after property getter full_name method:
# print (jane.full_name)  #//=> Jane Goodall

# # after property setter method:
# jane.full_name = "Tim Minchin"
# print(jane.__dict__)  #//=> {'first': 'Tim', 'last': 'Minchin', '_age': 0}
#_______________________________________________________________

# Parent/base class
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    # instance method
    def make_sound(self, sound):
        print(f"this animal says {sound}")

# child class; it inherits from Animal because of the "Animal" parameter passed into the Cat class
class Cat(Animal):
    
    def __init__(self, name, species, breed, toy):
        # super() refers to parent class of whatever the current class is; super inside of Cat class refers to Animal that is passed as parameter
        # with super, you don't have to specify "self", it will automatically be passed in
        super().__init__(name, species)

        # an option for refering to parent class to reduce duplication:
        # Animal.__init__(self, name, species)

        # self.name = name            #<-- this is duplication
        # self.species = species      #<-- this is duplication
        self.breed = breed
        self.toy = toy

    # init method can also be written as this below; since species will always be cat, remove "species from init parameters, and place in super() parameters with default value of "Cat"
    # def __init__(self, name, breed, toy):
    #     super().__init__(name, species= "Cat")
    #     self.breed = breed
    #     self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

    

buddy = Cat("Buddy", "Cat", "American Short Hair", "Ball")

# Cat class init method with duplication:
# print(buddy)  #//=> Buddy is a Cat

# # Cat class init method passing Animal.__init__(seld, name, species)
# print(buddy)  #//=> Buddy is a Cat
# print(buddy.species)  #//=> Cat
# print(buddy.breed)  #//=> American Short Hair
# print(buddy.toy)  #//=> Ball

# Cat class with super():
# print(buddy)  #//=> Buddy is a Cat
# print(buddy.species)  #//=> Cat
# print(buddy.breed)  #//=> American Short Hair
# print(buddy.toy)  #//=> Ball

# buddy.play() #//=> Buddy plays with Ball



# Animal
#     species
#     name 

# Cat
#     species
#     name
#     breed
#     favorite toy
#_______________________________________________________________

# Inheritance example: User and Moderator
class User:
    # the "self" keyword refers to the specific instance of the User class

    active_users = 0            # <-- class attribute; anytime a new user is created (initialized), we increment 1 to it; anytime we logout, we decrement 1 from it

    # class methods:
    # use this decorator to signifty that below it is a class method
    @classmethod
    # use the "cls" parameter, not the self parameter because it signifies that we'll be working with the acutual class
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    # this class method converts a string of data into a new instance
    # parameters are class and the data that's in string form
    def from_string(cls, data_str):
        # create 3 variables and assign the split data into them (split the data by commas)
        first, last, age = data_str.split(",")
        # return an instance using this class method with the data (this will run __init__, just like "user1 = User("Joe", "Smith", 68)")
        return cls(first, last, int(age))

    # init method:
    def __init__(self, first, last, age):
        # think of like self.variable_name = parameter, or self.key(in dictionary): value (parameter)
        self.first = first      # <-- instance attribute
        self.last = last        # <-- instance attribute
        self.age = age          # <-- instance attribute
        # anytime a new user is initialized, add one to active_users
        User.active_users += 1  # <-- refers to the class attribute/variable

    # __repr__ method (also an instance method)
    # when a user is printed, it turns this "<__main__.User object at 0x1027dc050>", into this "Tom is 89"; it turns it into a readable format that can be printed out
    def __repr__(self):
        return f"{self.first} is {self.age}"

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

    # setters (they change information)
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}!"

    def logout(self):
        User.active_users -= 1 
        return f"{self.first} has logged out."

class Moderator(User):

    total_mods = 0      # <-- class attribute; anytime a new moderator is created (initialized), we increment 1 to it

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        # anytime a new moderator is initialized, add one to total_mods
        Moderator.total_mods += 1

    # class methods:
    # use this decorator to signifty that below it is a class method
    @classmethod
    # use the "cls" parameter, not the self parameter because it signifies that we'll be working with the acutual class
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active mods."

    def remove_post(self):
        return f"{self.full_name} removed a post from {self.community}"


u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)

jasmine = Moderator("Jasmine", "O'Conner", 61, "Piano")
jasmine2 = Moderator("Jasmine", "O'Conner", 61, "Piano")

# print(jasmine.full_name()) #//=> Jasmine O'Conner
# print(jasmine.community) #//=> Piano
# print(User.display_active_users())  #//=> There are currently 5 active users.
# print(Moderator.display_active_mods())  #//=> There are currently 2 active mods.
#_______________________________________________________________

# Practice example 1.
# Roleplaying Game Classes
# Let's pretend we're building an RPG (roleplaying game) in Python. Side note: check out these games actually built in Python!
# 1. Define a base class "Character" that has the following properties:
# name  - String
# hp  - an Integer value representing health (aka hitpoints)
# level  - an integer value representing experience level
# 2. Define a subclass "NPC" (which stands for Non-Player Character) that inherits from Character , and has an additional instance method called speak  which prints the speech that character would say when a player interacts with them. 
# Example:
# villager = NPC("Bob", 100, 12)
# villager.name  # Bob
# villager.hp  # 100
# villager.level  # 12
# villager.speak()  # "I heard there were monsters running around last night!".
class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    pass


class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        return "{} says: 'I heard there were mosters running around last night!'".format(self.name)

villager = NPC("Bob", 100, 12)
# print(villager.name)  #//=> Bob
# print(villager.hp)  #//=> 100
# print(villager.level)  #//=> 12
# print(villager.speak())  #//=> Bob says: 'I heard there were mosters running around last night!'
#_______________________________________________________________

# Multiple Inheritances:

class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT")
        # i believe calls only the first parent
        super().__init__(name= name)
        # if you want both Aquatic and Ambulatory inits to run, you can just manually call them
        Aquatic.__init__(self, name= name)

    # or you can remove super() and just call both parents in init method (however, super() is the preferred way to reference the parent since it follows MRO automatically)
    # def __init__(self, name):
    #     print("PENGUIN INIT")
    #     Ambulatory.__init__(self, name= name)
    #     Aquatic.__init__(self, name= name)

# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
# captain_cook = Penguin("Captain Cook")

# Penguin instance is getting methods from both parent/base classes
# print(captain_cook.swim())  #//=> Captain Cook is swimming
# print(captain_cook.walk())  #//=> Captain Cook is walking

# # calls the greet from Ambulatory, not Aquatic, because Ambulatory is first parameter passed into Penguin class (see which print statements are run inside init method when a Penguin instance is made)
# print(captain_cook.greet())  #//=> I am Captain Cook of the land!

# Result with captain_cook is initialized:
# PENGUIN INIT
# AMBULATORY INIT

# if you want both Aquatic and Ambulatory inits to run, you can just manually call them, then all 3 print statements will run when Penguin instance is made
# Result when captain_cook is initialized after adding "Aquatic.__init__(self, name=name)" to Penguin init method:
# PENGUIN INIT
# AMBULATORY INIT
# AQUATIC INIT
#_______________________________________________________________

# Method Resolution Order (MRO) (super() is the preferred way to reference the parent since it follows MRO automatically):
# MRO: the order in which Python looks up (AKA resolves) methods on a class, influenced by inheritance

# B and C inherit from A, and D inherits from B and C
class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")
        # super called here refers to (D, B, C)
        super().do_something()

class C(A):
    def do_something(self):
        print("Method Defined In: C")
        # super called here refers to (D, B, C, A)
        super().do_something()

class D(B, C):
    def do_something(self):
        print("Method Defined In: D")
        # super called here refers to (D, B)
        super().do_something()


# ways to definitively determine the order:
# print(D.__mro__)  #//=> (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# print(D.mro())  #//=> [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# print(help(D))  #//=> takes you to a help menu that shows the order (use "q" to exit)  (the order is D, B, C, A, object)

thing = D()
# thing.do_something()  #//=> Method Defined In: D
#_______________________________________________________________

# Practice example 2.
# MRO Genetics
# Do you remember Gregor Mendel  from biology? We're going to simulate basic Mendelian inheritance in this exercise. You don't need to know what that means, but basically imagine a family where all the kids look exactly like one parent, maybe that parent has more "dominant" genetic traits than the other parent.
# Create three classes, Mother , Father , and Child .
# Let Mother have the "dominant" traits:
# eye_color = "brown"
# hair_color = "dark brown"
# hair_type = "curly"
# Let Father  have "recessive" traits:
# eye_color = "blue"
# hair_color = "blond"
# hair_type = "straight"
# Now define Child  to have the same attributes, eye_color , hair_color , and hair_type , but don't set them on the class.  Instead, let Child's Method Resolution Order be such that Child inherits from Mother  first, then Father .
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"
        
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"
        
class Child(Mother, Father):
    pass
#_______________________________________________________________

# Polymorphism and Inheritance:
# 1. Method overriding:

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass


# d = Dog()
# print(d.speak())  #//=> woof

# c = Cat()
# print(c.speak())  #//=> meow

# f = Fish()
# print(f.speak())  #//=> NotImplementedError: Subclass needs to implement this method
#_______________________________________________________________

# Special__magic__methods: below uses special methods to determine how "+" and "*" should work on our Human class

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    # this method uses the add operator to "add" two Humans and make a new Human:
    # self refers to whatever came first/the first operand (ie. j), and other refers to the second thing/the second operand that's added (ie. k)
    def __add__(self, other):
        # check to make sure it's a Human (if instance other, is Human)
        if isinstance(other, Human):
            # return a new Human with the attributes below
            return Human(first= "Newborn", last= self.last, age= 0)
        # if it's not a Human, return this string
        return "You can't add that!"

    # # this method clones Humans to make twins or triplets:
    # # self refers to whatever came first/first operand (ie. j), and other refers to the second thing/second operand that's added (ie. 2)
    # def __mul__(self, other):
    #     return "YOU ARE MULTIPLYING HUMANS!"

    # # this method clones Humans to make twins or triplets:
    # # self refers to whatever came first/first operand (ie. j), and other refers to the second thing/second operand that's added (ie. 2)
    # def __mul__(self, other):
    #     # check if other is an instance of int (if instance other, is int)
    #     if isinstance(other, int):
    #         # return list of new Humans for every i in range of other
    #         return [self for i in range(other)]
    #     return "Can't multiply!"

    # this method clones Humans to make twins or triplets:
    # self refers to whatever came first/first operand (ie. j), and other refers to the second thing/second operand that's added (ie. 2)
    def __mul__(self, other):
        # check if other is an instance of int (if instance other, is int)
        if isinstance(other, int):
            # return list of new Humans for every i in range of other
            # copy makes a new copy/space in memory for each copy so they are separate
            return [copy(self) for i in range(other)]
        return "Can't multiply!"


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)
# without repr method, print(j) //=> <__main__.Human object at 0x102f44f50>
# with repr method:
# print(j)  #//=> Human name Jenny Larson
# print(len(j))  #//=> 47

print(j + k)  #//=>  Human named Newborn Larson aged 0
# print(j + 2)  #//=>  You can't add that!

# first mul method:
# print(j * 2)  #//=>  YOU ARE MULTIPLYING HUMANS!
# the order matters: it looks for the first operand first
# print(2 * j)  #//=>  TypeError: unsupported operand type(s) for *: 'int' and 'Human'

# second mul method:
# print(j * 2) #//=> [Human named Jenny Larson aged 47, Human named Jenny Larson aged 47]
# print(j * "a") #//=> Can't multiply!

# triplets = j * 3
# # try to change the second object in the lists name to Jessica
# triplets[1].first = "Jessica"
# all have same name because they are all the same object, not a clone; this list is 3 references to the same thing
# print(triplets)  #//=>  [Human named Jessica Larson aged 47, Human named Jessica Larson aged 47, Human named Jessica Larson aged 47]

# third mul method (uses import statement at top of file); copy makes a new copy/space in memory for each copy so they are separate; below there are 3 copies:
# print(triplets)  #//=>  [Human named Jenny Larson aged 47, Human named Jessica Larson aged 47, Human named Jenny Larson aged 47]

# kevin and jessica having triplets:
# triplets = (k + j) * 3
# print(triplets) #//=>  [Human named Newborn Jones aged 0, Human named Newborn Jones aged 0, Human named Newborn Jones aged 0]
#_______________________________________________________________

# Special Methods and Inheritance:
class GrumpyDict(dict):
    # don't have to define init method because we inherit from dict; the init in dict will run instead because of MRO

    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        # returns the repr method we created for super(ie. dict) using the arguments passed when creating a new instance of GrumpyDict
        return super().__repr__()

    # called if the key is not in the dictionary; used to override it
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL IT AINT HERE!")

    # updates the data in the dictionary
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE...")
        # make the call below to add a new key value pair to the dictionary
        super().__setitem__(key, value)

    # checks if something is in the dictionary
    def __contains__(self, key):
        print("NO IT AINT IN HERE!")
        return False


data = GrumpyDict({"first": "Tom", "animal": "cat"})
# print(data) #//=> NONE OF YOUR BUSINESS
#             #//=> {'first': 'Tom', 'animal': 'cat'}

# before set item method:
# data["city"]  #//=> YOU WANT city? WELL IT AINT HERE!

# after set item method:
# data["city"] = "Tokyo"  #//=> YOU WANT TO CHANGE THE DICTIONARY?
#                         #//=> OK FINE...
# print(data)  #//=> NONE OF YOUR BUSINESS
#             #//=> {'first': 'Tom', 'animal': 'cat', 'city': 'Tokyo'}

# "city" in data  #//=> NO IT AINT IN HERE!
#_______________________________________________________________

# Practice example 3.
# Special Methods Train
# Create a class Train  that has one attribute: num_cars  which is specified when the train is instantiated.
# There should also be two special/magic/dunder methods on it:
# One method that describes the train when we call print  on it by saying "x car train" where x is the number of cars (see example below)
# One method that denotes the length of the train when we call len  on it
# Example:
# a_train = Train(4)
# print(a_train)  # 4 car train
# len(a_train)  # 4
# Note: You do not need to instantiate Train  for the tests to pass. The tests will try to instantiate Train  for you.
class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars
    
    def __repr__(self):
        return "{} car train".format(self.num_cars)
        
    def __len__(self):
        return self.num_cars
        
    pass

a_train = Train(4)
# print(a_train)  #//=> 4 car train
# print(len(a_train))  #//=>  4
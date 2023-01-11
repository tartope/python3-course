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
print(villager.name)  #//=> Bob
print(villager.hp)  #//=> 100
print(villager.level)  #//=> 12
print(villager.speak())  #//=> Bob says: 'I heard there were mosters running around last night!'
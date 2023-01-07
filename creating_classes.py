# Convention to name classes in singular and use upper camel case:

# class User:
#     # pass allows the code to move on, even though nothing is inside; so no error is returned
#     pass

# # creating an instance of this class (creates a new user); no need to explicitly call _init_() when creating an instance because Python knows to do it
# user1 = User()
# print(user1)  #//=> <__main__.User object at 0x10223c450>  (a user object was created; the alphanumeric string is the location in memory)
# print(type(user1)) #//=> <class '__main__.User'> (shows us its a class User)


class User:
    # when creating classes, almost always need an __init__ method (must be double underscore), and pass "self" as a parameter
    # the "self" keyword refers to the specific instance of the User class
    def __init__(self, first, last, age):
        # print("A new uswer has been made!")
        # think of like self.variable_name = parameter, or self.key(in dictionary): value (parameter)
        self.first = first
        self.last = last
        self.age = age

# user1 = User() #//=> A new uswer has been made!
# user2 = User() #//=> A new uswer has been made!
# user3 = User() #//=> A new uswer has been made!

user1 = User("Joe", "Smith", 68)
# print(user1.first, user1.last, user1.age) #//=> Joe Smith 68
user2 = User("Blanca", "Lopez", 41)
# print(user2.first, user2.last) #//=> Blanca Lopez
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

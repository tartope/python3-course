from say_sup import say_sup

def say_hi():
    print(f"Hi! My __name__ is {__name__}")

# before importing say_sup:
# say_hi()  #//=> Hi! My __name__ is __main__

# after importing say_sup:
say_hi()  
say_sup()

# we see the function called 3 times because:
# - say_sup() is being called in the say_sup.py file, then say_hi(), and say_sup() are being run in the say_hi.py file

# output before ignoring code on import, seen 3 times:
# Sup! My __name__ is say_sup
# Hi! My __name__ is __main__   <-- this is the main file being run so it gets the default of __main__
# Sup! My __name__ is say_sup   <-- this is the imported file so it gets the name say_sup


# Ignoring Code on Import (to prevent code from being run if it's not in the main file we are trying to execute): write below code in the other file (say_sup.py)
# if __name__ == "__main__":
#     # this code will only run
#     # if the file is the main file

#output after ignorning code on import
# Hi! My __name__ is __main__
# Sup! My __name__ is say_sup
def say_sup():
    print(f"Sup! My __name__ is {__name__}")

# say_sup()  #//=> Sup! My __name__ is __main__

# see say_hi.py file for explanation of below:
if __name__ == "__main__":
    say_sup()
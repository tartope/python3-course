from random import choice

def eat(food, is_healthy):
    # if is_healthy is false
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean!")
    # grab the ending in a variable
    ending = "because YOLO!"
    # if is_healthy is True, then set ending to the other sentence
    if is_healthy:
        ending = "because my body is a temple"
    # return an f string with the same sentence and pass in the argument and ending.  Must match the test exactly.
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept.  I didn't mean to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
    if person is "tim": return False
    return True

def laugh():
    return choice(("lol", "haha", "tehehe"))

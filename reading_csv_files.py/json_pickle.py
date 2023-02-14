import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name,
        self.breed = breed

c = Cat("Charles", "Tabby")

# frozen = jsonpickle.encode(c)
# print(frozen)  #//=> {"py/object": "__main__.Cat", "name": {"py/tuple": ["Charles"]}, "breed": "Tabby"}

# store in file:
# see cat.json file created with code below; it contains the same info as above print statement
# with open("cat.json", "w") as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open("cat.json", "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)  #//=> <__main__.Cat object at 0x101037fd0>

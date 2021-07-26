class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())#niko says woof!
print(felix.speak())#felix says meow!


"""
Polymorphism-
Both Nico and Felix share the same method name called Speak.
However, they are different types here ( <class '__main__.Dog'>, <class '__main__.Cat'> )
"""

# Way_1: iterate through different classes and happened to call the same method name
for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())

# <class '__main__.Dog'>
# <class 'str'>
# <class '__main__.Cat'>
# <class 'str'>


# Way_2 : Pass in some functions, and called method speak()
# pet and dog share the same method speak()
# pet_speak function takes in different pet object and calls different methods
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)#niko says woof!
pet_speak(felix)#felix says meow!
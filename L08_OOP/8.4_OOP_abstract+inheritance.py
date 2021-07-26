"""
abstract classes is one that never expects to be instantiated.
it never actually expect to create an instance of this class.
Instead, it's just designed to basically only serve as a base class.
"""

# Animal class is a base class
class Animal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

myanimal = Animal("fred")
#myanimal.speak() #NotImplementedError: Subclass must implement this abstract method

class Dog(Animal):
    def speak(self):
        return self.name + " says woof"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())#Fido says woof
print(isis.speak())#Isis says meow
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

myanimal = Animal() #ANIMAL CREATED
myanimal.eat() #I am eating
myanimal.who_am_i() #I am an animal

#Dog inherited from animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)#create an instance of animal class
        print("Dog Created")

    #override Animal's who_am_i() method
    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("WOOF")


mydog = Dog()
#ANIMAL CREATED
#Dog Created


mydog.who_am_i()#I am a dog!
mydog.eat()#I am eating
mydog.bark()#WOOF
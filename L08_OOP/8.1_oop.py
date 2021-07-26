#EX_1
class Sample():
    pass

my_sample = Sample()
print(type(my_sample))#<class '__main__.Sample'>

#EX_2
class Dog():
    def __init__(self,breed):
        self.breed = breed
my_dog = Dog(breed='Lab')

print(type(my_dog))
print(my_dog.breed)#Lab

#EX_3
class Cat:
    #Class object attribute
    #Same for any instance of a class
    species = "mammal"

    def __init__(self,breed,name,spots):
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #Expect boolean True/False
        self.spots = spots

    #Operations/Actions --->Methods
    def bark(self,number):
        print("WOOF!My name is {} and the number is {}".format(self.name,number))
        #注意format 是要寫self.name 而不是傳進物件的name
        #注意這邊number不需要寫self.number，是因為是直接從method的參數傳來，而不是物件本身

my_cat = Cat("Golden","Sammy",False)
print(type(my_dog))#<class '__main__.Dog'>
print(my_cat.breed)#Golden
print(my_cat.name)#Sammy
print(my_cat.spots)#False
print(my_cat.species)#mammal
print(my_cat.bark(5))

#EX_4
class Circle:
    #class object attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi  # attribute (ex: area)並不一定要是從()傳來的

    #Method
    def get_circumference(self):
        #return self.radius * self.pi * 2
        #因為pi是class attribute,寫Circle.pi較清楚
        return self.radius * Circle.pi *2


my_circle = Circle(30)
print(my_circle.pi)#3.14
print(my_circle.radius)#30
print(my_circle.get_circumference())#188.4
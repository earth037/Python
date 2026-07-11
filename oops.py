#Imperative Programming
# a = 2
# b = 3
# print(a+b)

#Functional Programming
# def add(a,b):
#     print(a+b)
# add(2,3)

#class
# class Car:
#     a = 2  #Attributes = variables defined inside class
#     def hello(): #Methods = functions defined inside class
#         print("Hello World" )

# print(Car.a) #Accessing Attributes
# Car.hello() #Accessing Methods
    
#Objects
# class Bags:
#     name = "ESNEarth"
#     def details(self):
#         print("this is a bag company")

# reebok = Bags() #creating object
# campus = Bags() #creating object
# print(reebok.name) #accessing attribute using object
# print(campus.name) #accessing attribute using object
# reebok.details() #accessing method using object
# campus.details() #accessing method using object

#Constructor
# class Bags:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

# reebok = Bags("Leather",2,3) #creating object
# campus = Bags("Canvas",3,4) #creating object
# print(reebok.material) #accessing attribute using object
# print(campus.material) #accessing attribute using object

#Types of Attributes and Methods
# class Animal:
#     a = 12 #Class Attribute

#     def __init__(self, name):
#         self.name = name #Instance Attribute

#     def hello(self): #Instance Method
#         print(f"Hello, I am a {self.name}")

#     @classmethod
#     def class_method(cls): #Class Method
#         print(f"This is a class method. Class attribute a = {cls.a}")

#     @staticmethod
#     def static_method(): #Static Method
#         print("This is a static method.")

# obj = Animal("Dog")
# obj.hello()
# obj.class_method()
# obj.static_method()

#Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def details(self):
#         print(f"This is {self.name}")

# class Humans(Animal):
#     pass

# obj = Animal("Lion")
# obj2 = Humans("Prithvi")
# obj2.details()

# class BagFactory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def details(self):
#         print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

# class Reebok(BagFactory):
#     def __init__(self,material,zips,pockets,color):
#         super().__init__(material,zips,pockets)
#         self.color = color

#     def details(self):
#         super().details()
#         print(f"Color: {self.color}")

# class Campus(Reebok):
#     def __init__(self,material,zips,pockets,color,brand):
#         super().__init__(material,zips,pockets,color)
#         self.brand = brand

#     def details(self):
#         super().details()
#         print(f"Brand: {self.brand}")

# bag1 = BagFactory("Leather", 2, 3)
# reebok = Reebok("Leather", 2, 3, "red")
# bag1.details()
# reebok.details()

# #Multiple inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Humans:
#     def __init__(self, id):
#         self.id = id

# class Robots(Animal, Humans):
#     def __init__(self, name, id):
#         Animal.__init__(self, name)
#         Humans.__init__(self, id)

#     def details(self):
#         print(f"Name: {self.name}, ID: {self.id}")

# robo = Robots("Robo1", 101)
# robo.details()

#Polymorphism
# Directly through class 
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Humans:
#     def speak(self):
#         print("Humans speak")

# obj1 = Animal()
# obj2 = Humans()
# obj1.speak()
# obj2.speak()

#Method overriding (we need inheritance)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def details(self):
#         print(f"This is {self.name}")

# class Humans(Animal):
#     def details(self):
#         print(f"This is a human named {self.name}")

# obj = Humans("Prithvi")
# obj.details()

#Duck Typing
# class Duck:
#     def talk(self):
#         print("Quack!")


# class Human:
#     def talk(self):
#         print("Hello!")


# class Robot:
#     def talk(self):
#         print("I am a robot.")


# class Dog:
#     def bark(self):
#         print("Woof!")


# def speak(obj):
#     obj.talk()


# # Creating objects
# duck = Duck()
# human = Human()
# robot = Robot()
# dog = Dog()

# # Calling the speak() function
# speak(duck)     # Duck object
# speak(human)    # Human object
# speak(robot)    # Robot object

# # This will raise an error because Dog doesn't have talk()
# speak(dog)

#Encapsulation
# class Factory:
#     __name = "Prithvi" #Private Attribute
#     a = 12 #Public Attribute
#     _age = 25 #Protected Attribute
#     def __init__(self, type, color):
#         self.__type = type #Private Attribute
#         self.color = color #Public Attribute

#     def __details(self): #Private Method
#         print(f"Type: {self.__type}, Color: {self.color}")

#     @classmethod
#     def info(cls): #Private Class Method
#         print(f"Factory Name: {cls.__name}")

# obj = Factory("Leather", "Red")
# print(obj.a) #Accessing Public Attribute
# Factory.info() #Accessing Private Class Method
# obj.__details() #Accessing Private Method (will raise an error)
# print(obj.__type) #Accessing Private Attribute (will raise an error)
# print(obj._age) #Accessing Protected Attribute

#Abstraction
# from abc import ABC, abstractmethod

# class enforce(ABC):
#     @abstractmethod
#     def enginestart():
#         pass

# class Bike(enforce):
#     def enginestart(self):
#         print("Bike engine started")

# class Car(enforce):
#     def enginestart(self):
#         print("Car engine started")



# obj1 = Bike()
# obj2 = Car()

#Dunder Methods
class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This is an animal named {self.name}"

    # def __len__(self):
    #     return len(self.name)

    # def __add__(self, other):
    #     return self.name + " and " + other.name

obj = Animal("Lion")
print(obj)  # Calls __str__ method

class Numbers:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
    def __eq__(self, value):
        return self.value == value.value

obj1 = Numbers(10)
obj2 = Numbers(10)

print(obj1 + obj2)  # Calls __add__ method and prints the result
print(obj1 == obj2)  #Calls __eq__ method and prints the result
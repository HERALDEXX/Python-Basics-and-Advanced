'''Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for encapsulation, inheritance, and polymorphism, making it easier to manage complex systems. OOP is widely used in modern software development and is a key feature of many programming languages, including Python.

A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. An object is an instance of a class, containing data and behavior defined by the class.'''


class Dog:
    """A class representing a dog."""
    def __init__(self, name, color, age, breed):
        """
        Initialize a new Dog instance with name, color, age, and breed.
        """
        self.name = name  # Instance variable for the dog's name
        self.color = color  # Instance variable for the dog's color
        self.age = age  # Instance variable for the dog's age
        self.breed = breed  # Instance variable for the dog's breed

    def bark(self):
        """Method to make the dog bark."""
        print(f"{self.name} says Woof! Woof!")

    def fetch(self, item):
        """Method to simulate the dog fetching an item."""
        print(f"{self.name} fetched the {item}!")

dog1 = Dog("Buddy", "Golden", 3, "Golden Retriever")  # Creating an instance of the Dog class
dog2 = Dog("Max", "Black", 5, "Labrador")  # Creating another instance of the Dog class

print(f"{dog1.name} is a {dog1.color} dog, is {dog1.age} years old and is a {dog1.breed}.")
print(f"{dog2.name} is a {dog2.color} dog, is {dog2.age} years old and is a {dog2.breed}.")
dog1.bark()  # Calling the bark method on dog1

class Animal:
    def speak(self):
        return "Animal makes a sound"
    
class Dog(Animal):
    def speak(self):
        return "Dog barks"
    
class Cat(Animal):
    def speak(self):
        return "Cat meows"
    
# Using polymorphism
animals = [Dog(), Cat()] # List of Animal objects
for pet in animals:
    print(pet.speak())    


# Duck typing example
class Duck:
    def sound(self):
        return "Quack! Quack!"    
    
class Person: 
    def sound(self):
        return "Hello!"
    
def make_sound(entity):
    print(entity.sound())

make_sound(Duck())
make_sound(Person())   
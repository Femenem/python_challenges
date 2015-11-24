#! /usr/bin/python3
class Animal:
	"""docstring for Animal"""
	def __init__(self, **kwargs):
		self._attributes = kwargs

	def set_attributes(self, key, value):
		self._attributes[key] = value

	def get_attributes(self, key):
		return self._attributes.get(key, None)

	def noise(self):
		print("Errr")

	def move(self):
		print("Moving Forward")

	def eat(self):
		print("Crunch, Crunch")

class Dog(Animal):
	def noise(self):
		print("Woof, Woof")
		super().noise()

class Cat(Animal):
	def noise(self):
		print("Meow")

def talkToMe(Animal):
	Animal.noise()
	Animal.eat()

jake = Dog()
sophoe = Cat()

talkToMe(sophoe)




#jake = Dog()
#print(jake.noise())
#print(jake.move())




#dog = Animal(name = "Puppy")

#dog.noise()
#dog.move()
#dog.eat()
#print(dog.get_attributes("name"))
#dog.set_attributes("Feet", 3)
#print(dog.get_attributes("Feet"))

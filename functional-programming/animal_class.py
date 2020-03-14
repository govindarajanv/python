class Animal:
    def __init__(self):
        print ("I am Animal's constructor")
    def eat(self):
        print ("I am eating")
    def attack(self):
        print ("I am attacking")
    def show_name(self):
        print ("I am an animal")

class Dog(Animal):
    def __init__(self):
        print ("I am Dog's constructor")
        super(Dog,self).__init__()
    def bark(self):
        print ("I am barking")
    def show_name(self):
        print ("I am a dog")

tommy = Dog()
print (tommy.bark())
print (tommy.show_name())
print (tommy.eat())
print (tommy.attack())


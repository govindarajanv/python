class Animal:
    "This is animal prototype"
    def __init__(self):
        print ("Animal is being created")
    def display(self):
        print ("I am an animal")
    def eat(self):
        print ("I am eating")

class Dog(Animal):
    "This is Dog prototype"
    def __init__(self):
        print ("Dog is being created")
        super().__init__()
    def display(self):
        print ("I am a dog")

nu = Dog()
print (nu.display())
print (nu.eat())
        

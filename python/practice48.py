class Animal:
    def __init__(self):
        print("Animal is a Mammal")
    
class Pet(Animal):
    def __init__(self):
        super().__init__()
        print("Pet is Animal")

class Dog(Pet):
    def __init__(self):
        super().__init__()
        print("Dog is Pet")

class Bark(Dog):
    def __init__(self):
        super().__init__()
        print("Dog Barks")
    
    def Barks(self):
        return "Children are scared of it"
b = Bark()
print(b.Barks())
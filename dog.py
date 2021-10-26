
import random

class Dog: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.bark()
        
    def bark(self, other=None):
        bark = random.choice(["woof", "ruff", "bork", "arf"])
        if other is None: 
            print(f"{bark}!")   
        else:
            print(f"{self.name} says {bark} to {other.name}.")
        
        
if __name__ == "__main__":
    d = Dog("Higgins", "labradoodle")
    print(f"{d.name} the {d.breed} says:")
    d.bark()
    d2 = Dog("tony", "rottweiler")
    d2.bark(d)
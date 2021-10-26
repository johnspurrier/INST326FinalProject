class Kennel: 
    def __init__(self):
        self.dogs = []
        
    def add_dog(self, dog): 
        self.dogs.append(dog)
        
    def remove_dog(self, dog): 
        self.dogs.remove(dog)
        
    def see_dogs(self): 
        for dog in self.dogs: 
            print(dog.name)
         

class Dog: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age
         
    def bark(self): 
        print("Woof!")
        
    def __gt__(self, other): 
        return self.age > other.age
    
    def __str__(self): 
        return f"{self.name} the Dog"
    
    def __repr__(self): 
        return f"Dog({self.name!r}, {self.age})"
        
class BarkyDog(Dog): 
    def bark(self): 
        super().bark()
        # Dog.bark(self) --> should never pass in a value of self 
        print("Yip!")
        
if __name__ == "__main__":
    d = Dog("Fido", 5)
    b = BarkyDog("Ralph", 3)
    print(f"{d.name} is about to bark")
    d.bark()
    print(f"{b.name} is about to bark")
    b.bark()
    
    k = Kennel()
    k.add_dog(d)
    k.add_dog(b)
    k.see_dogs()
    print(str(d))
    print(repr(d))
    
    
    
    
    # Pillars of OOP:
    # abstraction - come up with a natural interface that gives people access to what they need to have access to 
    # encapsulation - hiding the stuff that people don't need to see, tight coupling of data and functionality 
    # inheritance - child classes inherit methods from parent
    # polymorphism - optional parameters/arguments, magic methods to override default behaviors of operators
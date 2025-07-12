# how classes and objects work in Python
class Dog:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
    def bark(self):
        print(f"{self.name} says Woof!")
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age})"
    def __eq__(self, other):
        if isinstance(other, Dog):
            return self.name == other.name and self.age == other.age
        return False
    def __hash__(self):
        return hash((self.name, self.age))
    def __len__(self):  # returns the length of the dog's name
        return len(self.name)

# Example usage of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)
dog3 = Dog("Buddy", 5)
print(dog1)  # Output: Dog(name=Buddy, age=5)
print(dog2)  # Output: Dog(name=Max, age=3)
print(dog1.get_age())  # Output: 5
print(dog2.get_age())  # Output: 3  
dog1.bark()  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Max says Woof!
print(dog1 == dog2)  # Output: False
print(dog1 == dog3)  # Output: True
print(hash(dog1))  # Output: hash value of dog1
print(hash(dog2))  # Output: hash value of dog2
print(len(dog1))  # Output: 5 (length of the name "Buddy")
print(len(dog2))  # Output: 3 (length of the name "Max")
# Example of using the Dog class in a set
dog_set = {dog1, dog2}
print(dog_set)  # Output: {Dog(name=Buddy, age=5), Dog(name=Max, age=3)}


# Example of extending the Dog class
class ServiceDog(Dog):
    def __init__(self, name, age, service_type):
        super().__init__(name, age)  # Call the parent class constructor
        self.service_type = service_type  # Additional attribute for ServiceDog
    def perform_service(self):
        print(f"{self.name} is performing {self.service_type} service.")
    def __str__(self):
        return f"ServiceDog(name={self.name}, age={self.age}, service_type={self.service_type})"


# Example usage of the ServiceDog class
service_dog = ServiceDog("Rex", 4, "Guide")
print(service_dog)  # Output: ServiceDog(name=Rex, age=4, service_type=Guide)
# service_dog.bark()  # Output: Rex says Woof!
service_dog.perform_service()  # Output: Rex is performing Guide service.

# Example of inheritance and polymorphism
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def meow(self):
        print(f"{self.name} says Meow!")
    def get_age(self):
        return self.age
    def __str__(self):
        return f"Cat(name={self.name}, age={self.age})"

# Example usage of the Cat class
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 2)
print(cat1)  # Output: Cat(name=Whiskers, age=3)
print(cat2)  # Output: Cat(name=Mittens, age=2)
print(cat1.get_age())  # Output: 3
print(cat2.get_age())  # Output: 2
cat1.meow()  # Output: Whiskers says Meow!
cat2.meow()  # Output: Mittens says Meow!

# Example of polymorphism with Dog and Cat classes
def animal_sound(animal):
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()
    else:
        print("Unknown animal")

# Example usage of polymorphism
animal_sound(dog1)  # Output: Buddy says Woof!
animal_sound(cat1)  # Output: Whiskers says Meow!



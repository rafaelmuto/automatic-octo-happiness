
# This file explains and demonstrates the concept of "interfaces" in Python,
# covering the three main approaches:
# 1. Duck Typing (Informal)
# 2. Abstract Base Classes (ABCs) (Formal, Runtime-checked)
# 3. Protocols (Formal, Statically-checked)

# =============================================================================
#  1. Duck Typing (The Informal, Traditional Way)
# =============================================================================
print("--- 1. Duck Typing ---")

# The core idea: "If it walks like a duck and it quacks like a duck, then it
# must be a duck."
#
# In programming terms, this means an object's suitability for a task is
# determined by whether it has the necessary methods and properties, not by
# its specific class or type.

class Dog:
    """A simple class with a speak method."""
    def speak(self):
        return "Woof!"

class Cat:
    """Another class with a speak method."""
    def speak(self):
        return "Meow!"

def make_it_speak_duck_typing(animal):
    """
    This function doesn't care about the type of 'animal'. It only cares
    that the object passed to it has a .speak() method.
    """
    print(f"A {animal.__class__.__name__} says: {animal.speak()}")

print("Calling a function that relies on duck typing:")
dog = Dog()
cat = Cat()
make_it_speak_duck_typing(dog)
make_it_speak_duck_typing(cat)

# A class without a .speak() method would cause an AttributeError at runtime.
# class Human:
#     def make_noise(self): return "Hello"
# make_it_speak_duck_typing(Human()) # This would fail

print("\n" + "="*50 + "\n")


# =============================================================================
#  2. Abstract Base Classes (ABCs) (The Formal, Explicit Way)
# =============================================================================
print("--- 2. Abstract Base Classes (ABCs) ---")

# For situations where you need a more formal, explicit contract, you can use
# the `abc` module. This is closer to the traditional concept of an interface.
# An ABC defines a set of methods that a subclass *must* implement.

from abc import ABC, abstractmethod

# This is our "interface"
class Shape(ABC):
    """
    An abstract base class defining a contract for all shapes.
    Any concrete subclass *must* implement the 'area' method.
    """
    @abstractmethod
    def area(self):
        """A method that all subclasses must implement."""
        pass

# This class implements the Shape interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# This class also implements the Shape interface
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Trying to instantiate a class that doesn't implement the abstract method
# will result in a TypeError.
#
# class Triangle(Shape):
#     # This class is invalid because it doesn't implement area()
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
# my_triangle = Triangle(3, 6) # Raises TypeError at this line

print("Using classes that inherit from an ABC:")
my_circle = Circle(5)
my_square = Square(4)

print(f"Circle Area: {my_circle.area()}")
print(f"Square Area: {my_square.area()}")


print("\n" + "="*50 + "\n")


# =============================================================================
#  3. Protocols (Static Duck Typing)
# =============================================================================
print("--- 3. Protocols (Static Duck Typing) ---")

# A modern approach using the `typing` module. Protocols allow you to define
# interfaces that can be verified by static type checkers (like Mypy, Pyright).
#
# It's a formal, checkable version of duck typing. A class doesn't need to
# inherit from the protocol; it just needs to have the right structure.

from typing import Protocol

# This is our "interface" defined as a Protocol
class Speakable(Protocol):
    """A protocol that defines what it means to be 'speakable'."""
    def speak(self) -> str:
        ... # The body of a protocol method is not needed, use '...'

# --- These classes do NOT explicitly inherit from Speakable ---

class Human:
    """This class implicitly conforms to the Speakable protocol."""
    def speak(self) -> str:
        return "Hello, world!"

class Parrot:
    """This class also implicitly conforms to the Speakable protocol."""
    def speak(self) -> str:
        return "Polly wants a cracker!"

# This function is type-hinted to expect a Speakable object.
def make_it_speak_protocol(creature: Speakable):
    """
    A static type checker will verify that any object passed here
    has the methods defined in the Speakable protocol. At runtime, it
    behaves just like duck typing.
    """
    print(f"A {creature.__class__.__name__} communicates: {creature.speak()}")

print("Using a function that expects a Protocol:")
human = Human()
parrot = Parrot()

make_it_speak_protocol(human)
make_it_speak_protocol(parrot)

# A static type checker would flag an object that doesn't conform.
# For example, a `Car` class without a `speak` method would be caught
# by the type checker before you even run the code.

print("\n" + "="*50 + "\n")

print("Summary of Approaches:")
print("1. Duck Typing: Simple and flexible. Relies on runtime behavior. No formal contract.")
print("2. ABCs:         Formal and explicit. Requires inheritance. Enforced at runtime.")
print("3. Protocols:    Formal but implicit. No inheritance needed. Enforced by static type checkers.")

# OOP: Inheritance, Polymorphism and Abstract Classes (Python)

## 📌 Objective

To implement and understand the concepts of **Inheritance, Polymorphism, and Abstract Classes** in Python using Object-Oriented Programming (OOP).

---

# 📖 Theory

## 1. Inheritance

Inheritance is an Object-Oriented Programming (OOP) feature where one class (child/derived class) acquires the properties and methods of another class (parent/base class). It promotes **code reusability**, reduces duplicate code, and makes programs easier to maintain.

### Types of Inheritance in Python

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

---

## 2. Polymorphism

Polymorphism means **"many forms."** It allows the same method name to perform different tasks depending on the object.

### Example

- `Rectangle.area()`
- `Circle.area()`

Both classes use the same method name (`area()`), but each provides its own implementation.

---

## 3. Abstract Class

An **Abstract Class** is a class that cannot be instantiated directly. It contains one or more abstract methods that must be implemented by its child classes.

Python provides the **abc (Abstract Base Class)** module to create abstract classes.

---

# 📝 Algorithm

1. Import `ABC` and `abstractmethod` from the `abc` module.
2. Create an abstract class named `Animal`.
3. Declare an abstract method `sound()`.
4. Create child classes `Dog` and `Cat`.
5. Override the `sound()` method.
6. Create objects of `Dog` and `Cat`.
7. Call the `sound()` method.
8. Display the output.

---

# 💻 Python Program

from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass


# Child Class 1
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def display(self):
        print("Shape : Circle")
        print("Radius :", self.radius)
        print("Area :", round(self.area(), 2))
        print("-" * 25)


# Child Class 2
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def display(self):
        print("Shape : Rectangle")
        print("Length :", self.length)
        print("Width  :", self.width)
        print("Area :", self.area())
        print("-" * 25)


# Main Program
shapes = [
    Circle(5),
    Rectangle(10, 6)
]

# Polymorphism
for shape in shapes:
    shape.display()

# ▶️ Output

Shape : Circle
Radius : 5
Area : 78.54
-------------------------

Shape : Rectangle
Length : 10
Width  : 6
Area : 60
-------------------------
---

# 📚 Explanation

- `Animal` is an abstract class.
- `sound()` is an abstract method.
- `Dog` and `Cat` inherit from the `Animal` class.
- Both classes implement the `sound()` method differently.
- Calling the `sound()` method through different objects demonstrates **Polymorphism**.

---

# ✅ Features

- Demonstrates **Inheritance**
- Demonstrates **Polymorphism**
- Demonstrates **Abstract Classes**
- Uses Python `abc` module
- Beginner-friendly example

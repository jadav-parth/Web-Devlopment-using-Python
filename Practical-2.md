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

- `Circle.area()`
- `Rectangle.area()`

Both classes use the same method name (`area()`), but each provides its own implementation.

---

## 3. Abstract Class

An **Abstract Class** is a class that cannot be instantiated directly. It contains one or more abstract methods that must be be implemented by its child classes.

Python provides the **abc (Abstract Base Class)** module to create abstract classes.

---

# 📝 Algorithm

1. Import `ABC` and `abstractmethod` from the `abc` module.
2. Import the `math` module.
3. Create an abstract class named `Shape`.
4. Declare two abstract methods: `area()` and `display()`.
5. Create child classes `Circle` and `Rectangle`.
6. Override the `area()` and `display()` methods.
7. Create objects of `Circle` and `Rectangle`.
8. Store the objects in a list.
9. Use a loop to call the `display()` method for each object.
10. Display the area of each shape.

---

# 💻 Python Program

```python
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
```

---

# ▶️ Output

```
Shape : Circle
Radius : 5
Area : 78.54
-------------------------

Shape : Rectangle
Length : 10
Width  : 6
Area : 60
-------------------------
```

---

# 📚 Explanation

- `Shape` is an abstract class.
- `area()` and `display()` are abstract methods.
- `Circle` and `Rectangle` inherit from the `Shape` class.
- Both classes provide their own implementation of the `area()` and `display()` methods.
- Calling the `display()` method through different objects demonstrates **Polymorphism**.
- Inheritance allows the child classes to reuse the features of the parent class.

---

# ✅ Features

- Demonstrates **Inheritance**
- Demonstrates **Polymorphism**
- Demonstrates **Abstract Classes**
- Uses Python `abc` module
- Beginner-friendly example

---

# 🎯 Result

The program was executed successfully. It demonstrates the concepts of **Inheritance**, **Polymorphism**, and **Abstract Classes** using Python Object-Oriented Programming.

# OOP: Inheritance, Polymorphism and Abstract Classes (Python)

## 📌 Objective

To implement and understand the concepts of **Inheritance**, **Polymorphism**, and **Abstract Classes** using Python Object-Oriented Programming (OOP).

---

# 📖 Theory

## 1. Inheritance

Inheritance is an Object-Oriented Programming (OOP) feature where one class (child/derived class) acquires the properties and methods of another class (parent/base class). It helps in **code reusability** and reduces duplicate code.

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

Both classes use the same method name (`area()`), but each provides a different implementation.

---

## 3. Abstract Class

An Abstract Class is a class that **cannot be instantiated directly**. It contains one or more abstract methods that must be implemented by its derived classes.

Python provides the **abc (Abstract Base Class)** module for creating abstract classes.

---

# 📝 Algorithm

1. Import `ABC` and `abstractmethod` from the `abc` module.
2. Create an abstract class named `Shape`.
3. Declare abstract methods `area()` and `display()`.
4. Create child classes `Circle` and `Rectangle`.
5. Override the `area()` and `display()` methods.
6. Create objects of `Circle` and `Rectangle`.
7. Store the objects in a list.
8. Call the `display()` method using a loop.
9. Display the calculated area of each shape.

---

# 💡 Explanation

- `Shape` is an abstract class.
- `area()` and `display()` are abstract methods.
- `Circle` and `Rectangle` inherit from the `Shape` class.
- Both classes provide their own implementation of the `area()` and `display()` methods.
- Calling the `display()` method through different objects demonstrates **Polymorphism**.
- Inheritance allows both child classes to reuse the features of the `Shape` class.

---

# ✨ OOP Concepts Used

- ✅ Inheritance
- ✅ Method Overriding
- ✅ Polymorphism
- ✅ Abstract Class
- ✅ Abstraction

# Python Object-Oriented Programming (OOP) - A Complete Guide

## 📌 Overview
This repository contains a comprehensive guide to **Object-Oriented Programming (OOP) in Python** with detailed explanations, examples, and a **Chatbook Project** demonstrating all core concepts.

---

## 🏛 1. Class and Object in Python

### 🔹 What is a Class?
A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions).

### 🔹 What is an Object?
An **object** is an instance of a class, containing its own unique data and behavior.

### ✅ Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
    
    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}")

# Creating an Object
my_car = Car("Toyota", "Corolla")
my_car.display_info()  # Output: Car: Toyota Corolla
```

---

## 📌 2. Class Attributes and Methods

### 🔹 Attributes & Methods
- **Attributes** (Variables) hold data.
- **Methods** (Functions) define behavior.

### 🔹 Code Walkthrough
```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
s1 = Student("Alice", 20)
s1.greet()  # Output: Hello, my name is Alice and I am 20 years old.
```

### 🔹 Attributes vs. Methods
| **Attributes** | **Methods** |
|---------------|------------|
| Are accessed automatically | Need to be called explicitly |
| Hold data | Perform operations |

---

## 🤔 3. Why is Python Called OOP?
Python is called an **Object-Oriented Programming Language** because **everything in Python is an object**, including:
- **Data structures** (lists, tuples, dictionaries)
- **Data types** (int, str, float, bool)
- **Functions and modules**

```python
x = 10
print(type(x))  # Output: <class 'int'>

lst = [1, 2, 3]
print(type(lst))  # Output: <class 'list'>
```

---

## 🚀 4. Advantages of OOP in Python

### 🔹 1️⃣ Creating Custom Data Types
You can define **your own data types** using classes.

### 🔹 2️⃣ Code Reusability
Use **inheritance** to reuse existing code instead of rewriting it.

### 🔹 3️⃣ Easier Debugging
Encapsulation helps in **isolating issues** and debugging them faster.

### 🔹 4️⃣ Easy Collaboration
Multiple developers can **work on different classes** independently.

---

## 🏗 5. End-to-End OOP Project: Chatbook Class

### 🔹 Features:
- Demonstrates **functions vs. methods**
- Uses **dunder methods (magic methods)**
- Implements **Encapsulation, Getters & Setters, and Static Methods**

### ✅ Implementation:
```python
class Chatbook:
    def __init__(self, username):
        self.__username = username  # Private attribute (Encapsulation)
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def show_messages(self):
        for msg in self.messages:
            print(f"{self.__username}: {msg}")
    
    @property  # Getter
    def username(self):
        return self.__username

    @username.setter  # Setter
    def username(self, new_name):
        self.__username = new_name
    
    @staticmethod  # Static Method
    def app_info():
        print("Chatbook - A simple messaging app!")

# Creating an instance
user1 = Chatbook("Alice")
user1.add_message("Hello, world!")
user1.show_messages()

# Accessing static method
Chatbook.app_info()
```

---

## 🎯 Key OOP Concepts Used in Project

| Concept | Explanation |
|---------|------------|
| **Function vs Method** | Function is independent; Method belongs to a class |
| **Magic Methods** | Special dunder methods (`__init__`, `__str__`) |
| **Encapsulation** | Protects attributes using `_` or `__` (private attributes) |
| **Getter & Setter** | Used to control attribute access safely |
| **Static Method** | Independent function inside a class |

---

## 📌 Conclusion

- Python's **OOP model** makes programming more efficient.
- **Classes and Objects** allow structured code organization.
- **Encapsulation, Inheritance, and Polymorphism** enhance reusability and security.

📢 **Explore the code, experiment, and contribute! 🚀**

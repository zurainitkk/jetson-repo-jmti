# ==========================================
# INTRODUCTION TO PYTHON (IN CODE FORMAT)
# ==========================================

# Python is a high-level, interpreted programming language.
# It was created by Guido van Rossum and released in 1991.
# Python is easy to learn because of its simple syntax.
# Python is widely used in:
# - Web Development
# - Data Science
# - Artificial Intelligence & Machine Learning
# - Automation & Scripting
# - Game Development

# Features of Python:
# 1. Easy to read and write
# 2. Free and open-source
# 3. Platform independent (Windows, Linux, Mac)
# 4. Large standard library
# 5. Supports Object-Oriented Programming

# ==========================================
# FIRST PYTHON PROGRAM
# ==========================================

print("Hello, World!")
print("Welcome to Python Programming")

# ==========================================
# BASIC PYTHON NOTES (WITH CODE)
# ==========================================

# ---- Variables ----
x = 10              # integer
y = 2.5             # float
name = "Python"     # string
is_active = True    # boolean

# ---- Printing Values ----
print(x, y, name, is_active)

# ---- Checking Data Types ----
print(type(x))
print(type(y))
print(type(name))
print(type(is_active))

# ---- User Input ----
user_name = input("Enter your name: ")
print("Hello", user_name)

# ---- Type Casting ----
age = int(input("Enter your age: "))
print("Next year your age will be:", age + 1)

# ---- Operators ----
a = 20
b = 5

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division

# ---- Conditional Statements ----
if age >= 18:
    print("You are an Adult")
else:
    print("You are a Minor")

# ---- Loops ----
for i in range(1, 6):
    print("For loop value:", i)

count = 1
while count <= 5:
    print("While loop value:", count)
    count += 1

# ---- Lists ----
fruits = ["apple", "banana", "mango"]
print(fruits)
fruits.append("orange")
print(fruits)

# ---- Tuples ----
colors = ("red", "green", "blue")
print(colors)

# ---- Dictionary ----
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print(student)

# ---- Functions ----
def greet(name):
    print("Welcome", name)

greet("Student")

# ---- Error Handling ----
try:
    number = int(input("Enter a number: "))
    print(10 / nu

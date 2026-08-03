"""
17. type() Function
◽ The type() function is used to find type of a variables or value in python.

Syntax:
type (object)

# 🔹Examples:

x = 10 
y = 3.14
name = "Python"
print(type(x)) 
print(type(y))
print(type(name))

Output:
<class 'int'>
<class 'float'>
<class 'str'>


18.isinstance () Function ---
◽The instance() function is used to check whether an object belongs to a specific data type (class). 
It returns True if the object is of the specific type; otherwise, it returns False.

# 🔹Syntax:
isinstance(object, type)


# 🔹Examples:

x = 10
y = "Python"
print(isinstance(x, int)) # true
print(isinstance(y, str)) #true
print(isinstance(x, float)) # false

19. Input and Output in Python---

◽Input is used to take data from the user, and Output is uesd to display data on the screen.

🔹input() -> Takes input from the user
🔹print() -> Displays output on the screen

# 🔹Examples:

name = input("Enter your name:")
print("Welcome",name)

Output:Enter your name: Krutika
Welcome Krutika


🔴IMPORTANT POINT

`input()` always returns strings data. if you want number input, convert it using int() or float().

Taking integer input:

age = int(input("Enter your age: "))
print("Age:", age)

Taking decimal input:
marks = float(input("Enter marks:"))
print("Marks:",marks)
"""
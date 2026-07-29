"""
🔸---Variables in python----

 A Variables is a named memory location used to stored  data
 
 in simples words:
  A variables is a containerusedx tostore  data in a program.

  🔹For Example:


name = "Krutika"
age = 21
marks = 85.5
print(name)
print(age)
print(marks)

🔹Explaination
'name' stores a string value.
'age' stores an integer value.
`marks` stores a decimal value.
`print()` display the values on the screen.

2---How Variables Work in Memory---
 When a variable is created , python stores the values in the computer's memory and assigns a 
 name to that memory location.
  🔹For Example:

    x = 10
   🔹10 is stored in memory.

   🔹 x refers to the memory location containing 10.

   Variable      Value in Memory
   x   ───────────►   10

3.. Dynamic Typing in Python---

Dynamic typing means you do not need to declare the data type of a variable python automatically determines the type based on the value assigned.

🔹 Example no 1:
  x = 10
  x = 3.14
  x ="python"
  print(x)

  output:
  python

🔹 Example no 2:
    x = 10 print(type(x)) 
    x = "Python" print(type(x))

    output:
    <class 'int'>
    <class 'str'>



  key points:
  🔹No need to specify the data type.
  🔹A variable can store diffrent types of values.
  🔹Python automatically detects the variables data type.


4.Rules for Naming Variables-----
    🔹A variable name must start with a letters or an undercore(_).
    🔹It can no start with a number.
    🔹 It can contain letters, numbers,and underscores(_).
    🔹Python keywords (like if,for,class) cannot be used as variables names.

 🔹Example:
 name = "Krutika" #Valid
 _age = 20 #Valid
 1name = "John"  #Invalid
 class = "Python" #Invalid


5.Case sensitivity in python 

Python is case-sensitive, which uppercase and  lowercase letters are treated as different.

 🔹Example:
 age = 20
 Age = 25

 print(age) #output: 20
 print(Age) #output: 25

 Here, age and Age are two diffrent variables.
  
6.Multiple Assignment
 
Multiple assingment allows you to assign values ti mutiple variables in a single line.

🔹Example:

a,b,c = 10,20,30

print(a)
print(b)
print(c)



7.Constant in Python 

A constant  is a value that should not change during the excecution of a program.

Python does not have true constants, so programmers use UPPERCASE names to indicates constant values.

#SYNTAX
PI = 3.14
MAX_SPEED = 120


 #🔹Example NO. 1:
PI = 3.14
radius =  5
area = PI * radius * radius 
print("Area =", area)


 #🔹Example NO. 2:
MAX_SPEED = 120
print("Maximum Speed:", MAX_SPEED)

#ADVANTAGE
🔸Makes code easier to understand
🔸Improve maintainability by storing fixed values in one place.

9.Keyword and Identifiers
◽Keyword:
Keywords are reserved words in Python that have  a predefined meaning. 
They cannot be used as variables,function , or class names

 #🔹Example
  if
  esle
  for
  While
  True
  False

◽Identifiers:
Identifier are names given to variables ,function ,class or object by the programmer.

 #🔹Example

name = "Riya"
age = 20
total_marks = 85
  

Here, name ,age and total_marks are indentifiers
"""
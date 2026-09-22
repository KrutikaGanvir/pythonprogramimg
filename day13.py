'''
--------------- String in python ------------------------\


1. Concept Explanation

🔸Meaning of String

A string is a sequence of character (letters , numbers, symbols, or spaces)
enclosed inside quotes.

▫️Example:

  name = "Krutika"
  city = "Nagpur"

  Here,"Krutika"  and "Nagpur" are strings.

▪️Types of Quotes

a = 'hello':
b = "hello"
c = """hello"""

🔺Important Point:

String in Python are immutable, which means their characters cannot be changed directly  after creation


3.String Indexing

String indexing means accessing individual characters of a string using their position (index).

Python indexing start from 0.


▫️Example:

name = "Python"
print(name[0])
print(name[1])
print(name[5])

Index Position:

String: P  y  t  h  o   n 

Index:  0  1  2  3  4   5

Python  also supports negative indexing:

String:     p   y   t   h   o   n
Negative:  -6   -5  -4  -3  -2   -1

▫️Example


name = "Python"
print(name[-1])
print(name[-2])


Easy Trick: Positive index starts from 0 (left), negative index start from -1 (right)


4.String Slicing

String slicing means extracting a part of a string using index position.

Syntax:

string[ start : stop: step]

▫️Example:

name  = "Python"
print(name[0:3])
print(name[2:5])


▫️Example no:2

name = "Python"

print(name[:3])
print(name[2:])
print(name[::2])
print(name[:: -1])


🔹start =  where to start
🔹stop  = where to stop(not  include)
🔹step = how many position to jump


5.String Immutability

String immutability means that once  a string is created , its charaters cannot be changed directly.

▫️Example:

name = "Python"

name[0] = "j"

This will give an error because string cannot be modified directly.

Correct Way:

Create a new string:

name = "Python"
name = "j" + name[1:]

print(name)


👉 Immutable = Cannot be change directly.

So, Python strings are immutable.



Important String Methods:

String method are built-i n  function used to perform operation on strings.

Method                              Use                                 Example

upper()                            Convert to uppercase                 "hello".upper() --> HELLO

lower()                            Convert to lowercase                 "HELLO".lower()--> hello

capitalize()                      First letter uppercase                "python".capitalize()---> Python

title()                           First letter of each word             "hello world".title() ---> Hello world
                                  uppercase

strip()                           Renoves space from both ends          "hello ".strip() -- > hello

replace()                         Repalce  text                         "Hello".replace("H", "J") --> Jello

'''


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

split()                           Convert string into a list            "a b  c".split() --->  ['a', 'b' ,'c']

join()                            Join list/string elements             "-".join(["A","B"]) --->A-B

find()                            Find position of the                  "Python". find("t")--> 2

count()                           Count occurence                       "banana"..count("a") --> 3

startwith()                       Check starting text                    "Python". startwith("py")--->True

endswith()                        Checks  ending text                    "Python".endwith("on")c -- > True

isdigit()                         Checks whether  all are digits         "123".isdigit()--> True

isalpha()                        Checks whather all are letters           "Python".is alpha() -- > True


isalnum()                        Checks letters + numbers                 "Python123". isalnum() --> True


🔹Example:


text = "hello python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("python", "world"))
print(text.count("o"))



6.String Formating in python

String formatting means inserting variables or values  into a string in a clean  and readable way.


🔹Example:

1.Using f-string --

name = "Krutika"
age = 20

print(f"my name is {name} and i am {age} years old.")




2.Using format()


name = "Krutika"
age = 20

print("My name is {}  and I am {} year old." .format(name, age))

3.Formatting Numbers


price = 99.5678

print(f"Price = {price:.2f}")


 ▫️Here, .2f means 2 digits after the decimal point.



 8.Escape Characters

Escape characters are special characters used inside a string by using a backslash \.

They are used to represent things like a new line, tab, quotes, etc.



🔸Important Escape  Characters

    
Escape Character                   Meaning                        Example

\n                               New line                       "Hello\nWorld"
\t                               Tab space                       "Hello\tworld"
\\                               Backslash                       "C:\\Python"
\'                              Single quote                      'It\'s good'
\"                              Double quotes                      "he said \"Hello\""
\b                              Backspace                          "Hell\bo"


🔹Example:

print("Hello\nWorld")
print("Name:\tDipanshu")


'''

'''

----------- Tuple in python------------------------

1. Concept Explanation


What is Tuple 

 A tuple in Python  is a collection of multiple elements stored in a single  variable . A tuple is written usingn round brackets () and its elements are seperstes by commas.


 Example:

student = ("Rahul", 20, 85.5)

print(student)

2. Features of a Tuple


1.Ordered: Elements maintain their insertion order.
2.Immutable: Elements connot be changed after the tuple is created.
3.Duplicates allowed: The same value can apper mutilpes times.
4.Dioffrent data types: A tuple can store strings, integers, floats, etc.
5.Indexijng: Elements can be accessed using postitive and negative indexes.
6.Memory efficient:Tuples can use less memory than lists for comparable data.

3. Accessing Tuple Elements


fruits = ("Apple", "Mango", "Banana")

print(fruits[0])
print(fruits[-1])

4. Tuple Is Immutable

Once created ,tuple element cannot be modified



numbers = (10, 20, 30)
print(numbers)

5. Tuple vs List


Feature           Tuple                list

Changeable        ()                    []

ordered           No                    Yes

Duplicates       Allowed                Allowed


Example        (10, 20, 30)         [10, 20, 30]



6. Important Tuple Methods


Method                    Purpose

count()                   Count occurence of an element

index()                   Find the index of the first occrrence




numbers = (10, 20, 10, 30)


print(numbers.count(10))
print(numbers.index(20))

1. Tuple Indexing


Indexing means  accessing a particular element of a tuple using its index number.

Python indexing start from 0.



Example:

fruits = ("Apple", "Mango", "Banana", "Orange")

print(fruits[0])
print(fruits[1])
print(fruits[2])


2. Tuple Slicing


Slicing means accessing a portion of a tuple.

syntax:

tuple_name[start:stop:step]

start — index where slicing begins.

stop — index where slicing ends; this index is excluded.

step — interval between selected elements.


Example 1: Basic Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])



Example 2: Slice from the Beginning

numbers = (10, 20, 30, 40, 50)

print(numbers[:3])



Example 3: Slice to the End

numbers = (10, 20, 30, 40, 50)

print(numbers[2:])


Example 4: Using Step



numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])




Example 5: Reverse a Tuple



numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])


🔸Tuple Immutability


1. Meaning of Tuple Immutability
Tuple immutability means that once a tuple is created, its elements cannot be changed, added, or removed directly.

In Python, tuples are immutable, unlike lists, which are mutable

2. Example of Tuple Immutability


numbers = (10, 20, 30)

print(numbers)

numbers[0] = 50

print(numbers)


Output:


(10, 20, 30)
TypeError: 'tuple' object does not support item assignment


3. Can We Add or Remove Elements?

fruits = ("Apple", "Mango", "Banana")


print(fruits)

Tuples do not support list method such as append() and remove().


4. How to Make Changes to a Tuple

You can convert a tuple into a list, modify the list, and convert it back into a tuple.



numbers = (10, 20, 30)

temp = list(numbers)
temp[0] = 50
numbers = tuple(temp)

print(numbers)

'''




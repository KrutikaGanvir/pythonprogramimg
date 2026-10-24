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


'''

numbers = (10, 20, 10, 30)


print(numbers.count(10))
print(numbers.index(20))






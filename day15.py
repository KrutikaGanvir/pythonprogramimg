'''

#....................List in Python................................

🔹Meaning of List in Python

A list in Python is a collection of multiple items stored in a single variable. A list is written using square bracket[], and its elements are seperated by commas.


🔸Examplev No:  1. Create and print a list

fruits = ["Apple", "Mango", "Banana", "Orange"]
print(fruits)



🔸Example No: 2. Take a list of numbers and print it

numbers = [10, 20, 30, 40,50]
print(numbers)

🔸Example No: 3. Access list elements using indexing



fruits = ["Aplle" , "Mango" , "Banana"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])


▪️Logic: 

Indexing start at 0. Negative index -1 refers to the last element.

🔹Features of List

1. Ordered:List elements maintain their order of insertion.
2.Mutable:Element can be added, removed, or change after creating a list.
3.Allows Duplicates: A list can duplicate values.
4.Diffrent Data Types: A list can store integers, string, floats, and other data btypes together.
5. Indexing:Element can be accessed sing positive and negative indexes.
6.Dynamic Size: A list can grow or shrinkl as element are added or removed.
7.Slicing: We can access a portion of a list using slicing.
8.Nested list:A list can contain other lists as elements.


🔸Example :


data =[ 110, "Hello", 20, 10]
print(data[0])    # indexing
print(data[1:3])   #Slicing
data[0] = 50       # Modification
data.append(30)      # Adding an element

print(data)


🔹Accessing List Elements

List elements are accessed using index numbers. Python indexing starts from 0.

1. Positive Indexing:


fruits = ["Apple", "Mango", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


2. Negative Indexing


fruits = ["Apple", "Mango", "Orange"]
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])


3. Accessing Using a Variable

numbers  = [10,20,30,40,50]

i = 2
print(numbers[i])


4. Accessing Multiple Elements — Slicing


numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Prints elements from index 1 to 3
print(numbers[:3])   # Prints elements from the beginning to index 2
print(numbers[2:5])  # Prints elements from index 2 to 4
print(numbers[::2])  # Prints every second element


5. Accessing All Elements Using a Loop

numbers = [10, 20, 30, 40, 50]
for n in numbers:
    print(n)
'''
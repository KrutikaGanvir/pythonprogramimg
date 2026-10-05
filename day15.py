'''

#....................List in Python................................

🔹Meaning of List in Python

A list in Python is a collection of multiple items stored in a single variable. A list is written using square bracket[], and its elements are seperated by commas.


🔸Example No:  1. Create and print a list

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


🔹Changing List Values   

Python lists are mutable, which mneans we can  change their elements after creating the list.

We can change a list value by using its index number.


🔸Example No: 1. Change a Single Value

fruits = ["Apple", "Mango","Banana"]
fruits[0] = "Orange"
print(fruits)



🔸Example No:2. Change Multiple Values

numbers = [ 10, 20, 30, 40, 50]

numbers[1:3] = [25, 35]
print(numbers)

🔸Example No: 3. Change the Last Value

names = [ "Rahul" , " Amit", "Rohit"]
names[-1] = "Vijay"
print(names)

🔸Example No: 4.changing the values using user input

numbers = [10, 20, 30]

new_values = int(input("Enter new values:"))
numbers[1] = new_values
print(numbers)


🔹Important List Methods

List method are built-in function used to add, remove, change, serach, and arrange element in list.

1. append()

🔸Example: Adds an element at the end of the list.

numbers = [ 10, 20, 30]
numbers.append(40)
print(numbers)


2. insert()

🔸Example: Adds an element at a specific index.

numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)



3. remove()

🔸Example: Removes  a specific value.

numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)


4. pop()

Removes an element using its index. if no index is given , is given , it removes the last element.

numbers = [10,20,30,40]
numbers.pop(1)  
print(numbers)


5. clear()
Removes all elements from the list.


numbers = [10,20, 30]
numbers.clear()
print(numbers)



6.sort()

Arranges elements in ascending order.

numbers = [40,10,30,20]
numbers.sort()
print(numbers)



7.reverse()

Reverse the order of elements.

numbers = [10, 20,30, 40]
numbers.reverse()
print(numbers)


8. count()
Count how many times a value occurs.


numbers = [10, 20,10, 30,10]
print(numbers.count(10))

9.index()

Returns the index of the first occurrence of a value.


fruits = ["Apple", "Mango", "Orange"]
print(fruits.index("Mango"))

10.copy()

Create a copy of a list.


numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)



🔹append() vs extend()

 Both method are used to add elements to a list, but they work diffrently.

 1.append() adds the entire object as one singlen element at the end of the list.

 🔸Example:

numbers = [1, 2, 3]

numbers.append([4,5])
print(numbers)

2.extend()
'''
numbers = [1, 2,3]

numbers.extend([4,5])
print(numbers)




'''
#-------------------------------Practice Problems -------------------------------------


1. Find Maximum Element
numbers =  [10, 45, 23, 89, 12]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:" , maximum)

2. Remove Duplicate Elements


numbers = [10, 20, 10, 30, 20]
unique = []
for num in numbers:
    if num not in unique:
     unique.append(num)
print(unique)    


 3.Second Largest Number


numbers = [10, 45, 23, 89, 12]
numbers.sort()
print("Second largest:" , numbers[-2])

4. Create a list of 5 student names and print all names.

students = ["Rahul" , "Amit" , "Priya" , "Sneha", "Rohit"]

print("Student Names")

for name in students:
    print(name)


 5. Find sum of all elements in a list.
 



numbers = [10, 20, 30, 40,50 ]
total = 0

for num in numbers:
    total = total + num

print("Sum of all elements =" , total)

6.find minimum element from a list .

'''
numbers = [25, 10, 45, 5, 30]

minimum = numbers[0]

for num in numbers:
    if num > minimum:
        minimum = num
print("Minimum element =" , minimum)
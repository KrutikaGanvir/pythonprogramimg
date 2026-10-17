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


numbers = [25, 10, 45, 5, 30]

minimum = numbers[0]

for num in numbers:
    if num > minimum:
        minimum = num
print("Minimum element =" , minimum)

7. Remove duplicate elements from a list.



numbers = [10, 20, 10, 30, 20, 40]

unique = []

for num in numbers:
    if num not in unique:
         unique.append(num)
print("List after removeing duplicates:" , unique)  


8.Count frequency of each element.


numbers = [10, 20, 10 , 30, 20, 10]

for num in numbers:
    if numbers.index(num) == numbers.index(num):
        print(num, "occurs", numbers.count(num),"times")



9 Merge two lists.



list1 = [10, 20, 30]
list2 = [40, 50, 60]

merged_list = list1 + list2

print("Merged list=", merged_list)


10.Sort a list without using sort().



numbers = [40,10, 30, 20, 50]

n = len(numbers)

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
         numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list =",numbers)


11. Rotate a list by one position.


numbers = [10,20, 30,40,50]
last = numbers.pop()


numbers.insert(0 , last)

print("Rotated list =", numbers)


12. Move all zeroes to the end.




numbers = [0,1 ,0, 3, 12,0 , 5]
result = []
for num in numbers:
    if num != 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

print("Update list =" , result)               



 13.Create a list of 5 student names and print all names.


students = [ "Rahul" , "Amit" , "Priya" "Sneha", "Rohit"]

for name in students:
    print(name)




13.Find sum of all elements in a list.
    

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
     total = total + num


print("Sum of all elements = " , total) 


14.Find minimum element from a list.

'''

numbers = [25, 10, 45, 5, 30]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum element =", minimum)       

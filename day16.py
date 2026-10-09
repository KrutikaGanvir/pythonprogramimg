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
'''

numbers = [10, 45, 23, 89, 12]
numbers.sort()
print("Second largest:" , numbers[-2])


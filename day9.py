'''
--------------------------Practice Problem-----------------  

1. Write a program to check whether a number is greater than 100 or not.

 
num = int (input("Enter a number:"))
if num > 100:
    print("The number is greater than 100.")
else:
    print("The number is not greater than 100.")

    
2. Write a program to check whether marks are pass or fail.


marks = int(input("Enter your marks:"))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


3. Write a program to check whether a number is even or odd.

    
num = int(input("Enter a number:"))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

    

4. Write a program to check whether a number is positive, negative, or zero.


  

num = int(input("Enter a number:"))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

    

20. Write a program to find the smallest of two numbers.
      ''' 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 < num2:
   print("The smallest number is:", num1)
else:
   print("The smallest number is:", num2)


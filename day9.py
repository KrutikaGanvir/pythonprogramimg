'''
--------------------------Practice Problem-----------------  

🔸1. Write a program to check whether a number is greater than 100 or not.

 
num = int (input("Enter a number:"))
if num > 100:
    print("The number is greater than 100.")
else:
    print("The number is not greater than 100.")

    
🔸2. Write a program to check whether marks are pass or fail.


marks = int(input("Enter your marks:"))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


🔸3. Write a program to check whether a number is even or odd.

    
num = int(input("Enter a number:"))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

    

🔸4. Write a program to check whether a number is positive, negative, or zero.


  

num = int(input("Enter a number:"))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

    

🔸5. Write a program to find the smallest of two numbers.
     
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 < num2:
   print("The smallest number is:", num1)
else:
   print("The smallest number is:", num2)

   

🔸6. Program to Find the Largest of Three Numbers 


a = 10 
b = 25
c = 15

if a > b and a > c:
    print("Largest =", a)
elif b > a and b > c:
    print("largest =", b)
else:
    print("Largest =", c)

    
🔸7.Program to Check Driving License Eligibility   
     

age = int(input ("Enter your age:"))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

🔸8. Write a program to check whether a number is divisible by 7.

   
num = int(input("Enter a number:"))

if num % 7 == 0:
    print("The number is divisible by 7")
else:
    print("Number is not divisible  by 7")

    
🔸9. Write a program to check whether username and password are correct.
     
username = input("Enter username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login sucessful")
else:
    print("Invalid username or password.")


   🔸10.. Write a program to print grade using marks. 
 

marks = int (input("Enter your marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print ("Grade F")


🔸11. Write a program to check whether a year is leap year.

     '''

year = int(input("Enter a year:"))

if year  % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")

else:
    print ("Not a leap year")
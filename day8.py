'''
---------------------12. Real-Life Programs Using Conditional Statements-------------------------

🔸Program 1: Greatest of Two Numbers

a = 25
b = 40
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

    

🔸Program 2: Greatest of Three Numbers

a = 10
b = 25
c = 15
if a >= b and a >= c:
    print("a is greatest")
elif b >= c:
    print("b is greatest")
else:
    print("c is greatest")

🔸Program 3: Simple Calculator 

a = 10
b = 5 
operator = "+"

if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print("Invalid operator")



🔸Program 4: Discount Calculator  


amount = 6000

if amount >= 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.05

final_amount = amount - discount
print("Discount : ", discount)
print("Final amount to be paid: ", final_amount)

🔸Program 5: Check leap Year


year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

 🔸Program 6: Traffic Signal   

signal = "red"

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")



🔸Program 7: Number Dvisible By 5 and 11
   

num = 55
if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11")
else:
    print(num, "is not divisible by both 5 and 11")


🔸Program 8: Basic Login System

username = "krutika"
password = "krut@123"

if username == "krutika" and password == "krut@123":
    print("Login successful!")
else:
    print("Invalid credentials!")
'''
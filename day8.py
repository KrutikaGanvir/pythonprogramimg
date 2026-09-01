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
'''

amount = 6000

if amount >= 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.05

final_amount = amount - discount
print("Discount : ", discount)
print("Final amount to be paid: ", final_amount)

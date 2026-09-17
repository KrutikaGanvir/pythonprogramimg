'''

--------------------PRACTIC SET 2--------------------------------

1.Print numbers from 10 to 1 using while loop.


i = 10

while i >= 1:
    print(i)
    i = i - 1


▪️Logic: 
 🔹Start with i = 10
 🔹Run loop while i >= 1
 🔹i = i - 1 decreases the number by 1 each time

 
 2.Print table of 5.

for i in range(1, 11):
     print("5 x" , i, "=", 5 * 1)

▪️Logic: 

range(1, 11) runs the loop from1 to 10 , and each time 5 * i calculates the table.


3.Find sum of digits of a number.
      
num = int(input("Enter a number:"))
total = 0

while num > 0:
    digit =  num % 10
    total = total + digit
    num = num // 10

print("Sum of digit =" , total)    



▪️Logic: 

1 + 2 + 3 + 4 + 5 + = 15

👉 % 10 ---> gets the last digit
👉 // 10 ---> remove s the last digit
 '''
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
▪️Logic: 
👉 % 10 ---> gets the last digit
👉 // 10 ---> remove s the last digit


4. Check Armstrong number.

An Armstrong number is a number whose sum  of  each digit raised to the powweer of the number5 of digits is equal ton the original number.

🔹Example:153

 1³ + 5³ + 3³ = 153




num = int(input("Enter a number:"))
original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if total == original:
    print(" Armstrong number") 
else:
    print("Not an Arnstrong number")



5. Print multiplication tables from 1 to 10.
     
for i in range(1, 11):
     
     print("Table of", i)

     for j in range(1, 11):
        print(i ,"x" , j, "=" ,1 * j)

        
▪️Logic: 
outer loop(i) --> select table 1 to 10

inner loop(j)---> print each table from 1 to 10.
        
'''
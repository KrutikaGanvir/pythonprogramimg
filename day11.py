'''

#-----------------  Practice problems -----------------------

1.Print numbers from 1 to 100.

for i in range(1, 101):
    print (i)

    
▪️Logic:
range(1, 101) start from 1 and stop before 101, so it print 1 to 100.

range(start, stop) ---> stop number is not included.


2.Print even and odd numbers.


for i  in range(1,11):
    if i % 2 ==  0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

▪️Logic:     

🔹i  % 2 == 0 ---> Even
🔹Otherwise ---> Odd

% gives the remainder after division


3.Find sum of natural numbers.


num = int(input("Enter a number:"))
total = 0

for i in range(1, num + 1):
    total = total + i

    print("Sum =" , total)


▪️Logic:   

For 10: 1 + 2 + 3 + ...... + 10 = 55

total = total + i adds each number to the total

4.Find factorial of a number.
  
num = int(input("Enter a number:"))
fact = 1

for i in range(1, num + 1):
    fact = fact * i
    print("Factorial =", fact)

▪️Logic: 

5! = 5 * 4 * 3 * 2 * 1 = 120

Factorial = Multiplication of al, positive number from 1  to that number.


5.Check prime number.
 

num = int(input("Enter a number:"))

if num < 2:
    print(" Not a prime number")

else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
            print("prime number")
    else:
         print("Not a prime number")


  
▪️Logic: 
A prime number is a number that is divisible by only 1 and  itself.


if any number from 2 to num- 1  divided it exactly --> Not Prime.


6.Reverse a number.


num = int(input("Enter a number: "))

reverse = 0
while num > 0:
    digit = num % 10
    reverse =  reverse * 10 + digit
    num  = num
 

print*("reverse =" , reverse)
  
 

▪️Logic: 

🔹num % 10 -- > gets the last digit.
🔹reverse * 10 + digit --> adds the didgit  to the reverse number.
🔹num // 10  --- > remove the last gdigit.


 '''
'''
#  -------------------------------Loops in Python---------------------------------------

1.Concept of Eplanation 

🔸Meaning of looop  
A loop is used to repeat a block of code agian and again Without loops, we need to write the same many times.


EX:If we want to print  numbers from 1 to 100, writing 100 printnsatement is not a good method Aloop can do this work easily



🔹Simple Example:


for i in range(1,100):
    print(i)


🔸 Why Loops Are Used in Python

Loops are used  to repeat  a block of code multiople times without writing the same code again and again.

Main Uses of Loops:

1. To repeat a task mutliple times.
2. To process multiple value one by one.
3. To save time and reduce code repetition
4. To perform calcution repeatedly.
5. To work with lists , strings, and other collections.


Example:
 Without  loop:

 print(1)
 print(2)
 print(3)
 print(4)
 print(5)

 Using loop:


for i in range(1, 6):
    print(i)

    
 ▪️range() Function in python  

 The range()  function is used to gererated a sequence of numbers, mainlly  with for loops.

SYNTAX:
  range(start , stop , step)

  🔹start --> Starting number
  🔹stop ---> Ending  limit (Not including)
  🔹step --> Diffrent betwwen numbers

Example:

for i in range(2, 11, 2):
print(i)


🔸Whlie Loop 

A while loop is used ton repeat a block of code as long as  a given condition is True.


Syntax:

while condition:
    # code to repeat

🔹Example:

i = 1
while i <= 5:
    print(i)
    i = i + 1

    
🔺How it works

🔹 i = 1 1  --> starting value
🔹 i <= 5 --> condition 
🔹 i = i + 1 --> increases i after every loop
🔹When i becomes 6, condition becomes False, so the loop stops.

🔸break Statement:

The break statement is used to immediate stop a loop ,even if the loop condition isn still true.

🔹Example:

for i in range(1, 6):
 if i == 3:
  break
 print(i)
    
 When i becomes 3, break stops the loop


 🔸Pass Statement:

 The pass statement is used when you want to leave a block of code empty without causing an error.

 It acts a placeholder for code that you will write later.


 🔹Example:

for i in range(5):
 pass
    
 
 print("Loop completed")

🔹Example no:2



age = 20

if age >= 18:
    pass
else:
    print("Not eligible")

    
 Here,pass means Do nothing / placeholder   


 🔸Nested Loop

for i in range(1,4):
   for j in range (1,4):
     print(i ,j)



How it Works:

🔹 Outer loop --> i
🔹Inner loop --> j
🔹For every value of i, the inner loop runs 3 times.


''' 
#--------------Conditional Statements in Python-------------------

 #🔸1. What is a Conditional Statement?
'''


Conditional statement are used to make decision in a Python propgram based on wheather a condition is True or False.

🔹Simple Example:

age = 18

if age >= 18:
print(""you are eligible to vote")

Types of Conditional Statements

1.if Statement - Execute ciode when a condition is  true.
2.if-else Statement - Chooses between two conditions.
3.if-else-else Statement - Check multiple condition.
4.Nested if Statement - An if statement inside another if.
5.Conditional Expression (Ternary Operator)-Short form  of if - else .







2. Why Do We Use Conditional Statements?

Conditional statement are used to make decision in aprogram based on a given condition.

They help the program excecute code for diffrent situations.

age = 20
if age >= 18:
    print("Eligible to vote")

else:
    print("Not eligible to vote")  






3. Important Operators Used in Conditions------

◽In python , operators are symbols or keywords used to compare values and combine conditions. They are mainly used if , elif , and else statements.

1.Comparison Operators

Comparison operators compare two values and return either True or False.

Operator                     Meaning                               Example              Result 
==                           Equal to                              5 == 5               True
!=                           Not equal to                          5 != 3               True
>                            Greater than                          5 > 3                True
<                            Less than                             5 < 3                False
>=                           Greater than or equals to             5 >= 5              True
<=                           Leass than or equal to                3 <= 5              true




🔹Simple Example:

age = 20

if age >= 18:
print("You are eligible to vote.")




2.Logical Operator

◽Logical opreator are used to combine multiple conditions.

-----------------
🔺and
Returns True only when both condition are true.

🔹# Example:

age = 20 
marks = 75

if age >= 18 and marks >= 50:
print("Eligible")


--=---------------

🔺or
Returns True when at least one condition is true.


🔹# Example:

age = 17 
has_permission = True

if age >= 18 or has_permission:
     print("Allowed")

     
-----------------  

🔺not
 Reverse the result of a condition.

 is_raining = False

 if not is_raining:
   print("you can go outside.")



3.Membership Operator

Membership operator check whether a value exists inside a sequence such as a list,tu[le,string,etc

▪️in -->  value exists
▪️not in --> value does not exist

🔹# Example:

fruits =[ "apple" , "banana", "mango"]

if "mango" in fruits:
    print("Mangon is available.")




4. Identitty Operators

Identify operators check whether two variables refer to the same object.

▪️is 
▪️is not  

🔹# Example:
    
a = None

if a  is None:
    print("No value")

IMPORRTANT NOTE:

==  Check wether two values are equal , while is check whether they are the same object.
---------------------------------------------

4.Indentation in Condition Statement 

Indentation means giving spaces at the beginning of a line to show which statement belong to a conditional block.

Python uses indentation  to define the  block of code.

🔹# Example:

age = 18

if age >= 18:
    print("You can vote")
 

Here, the space before print()  shows that it belongs to the if statement .  


IMPORRTANT NOTE:

🔸Usually 4 spaces are uesd for indentation.

🔸Incorrect indentation  caues an IndentationError.

5. If Statement in Python

The if statement is used to execute a block of code only a given condition is True.

▪️Syntax:

if condition:
    statement



🔹# Example:

age = 20

if age >= 18:
print("Eligible to vote")

6.If - else statement in Python

The if -else statement is uesd to choose between two blocks of code.

🔸If the condition is True --> if block runs.

🔸If the condtion is False --> else block runs.

▪️Syntax:

if condition:
    statement1
else:
    statement2    

🔹# Example:

age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print ("Not eligible to vote")

----------------------------------------------------------------------
 🔺More Examples of if-else Statement

 ex no 1:Check Even Or Odd

   
num = 10 
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
------------------------------------------


 ex no 2:Check Pass or Fail
    

marks = 35

if marks >= 40:
    print("pass") 
else:
    print("Fail")

    

 ex no 3:Check Positive   or Negative
      

num = -5

if num >= 0:
    print("Positive Number")

else:
    print("Negative Number")    
-----------------------------------------------------


7.if-elif-else Statement in Python


DEFINITION:
◽The if-elif-else  statement is used to check multiple conditions.
🔹if --> checks the first condition.
🔹elif --> Checks another condition if the previous condition is False.
🔹else ---> Runs when all condition are False.


Syntax:

if condition:
    statement
  elif condition2:
    statement
  else:
    statement


🔹# Example:Grade

marks = 75

if marks >= 90:
    print ("Grade A+")
elif marks >= 60:
    print ("Grade A")
else:
    print ("Grade B")



'''


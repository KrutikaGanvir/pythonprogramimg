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

    '''


"""
    22.OPERATION IN PYTHION-------------

◽Operation are special sysmbol used to perform operations on values and variables in Python

🔹Example:
a = 10
b = 5
print(a + b)

🔸Types of Operators

1.Arithmatic --> +, -,*, /, %
2.Comparison --> ==, !==, >,<
3.Logical --> and, or, not
4.Assignment --> = , +=, -=
5.Membership --> in ,not in
6.Identity --> is, is not

🔹Example:

a = 10
b = 5

print( a + b)
print( a > b)

23. Arithmatic Operator in Python 

Arithmatic Operator are used to perform basic mathematical operations on numbers.

Operatorr           Meaning                 Example
 +                  Addtion                 10 + 5 = 15
 -                  Subtraction             10 - 5 = 5   
 *                  Multiplication          10 * 5 = 50
 /                  Division                10 / 5  =2.0
 %                  modulus(remainder)      10 % 3  = 1
 //                 Floor Division          10 // 3 = 3
 **                 Exponentiation          2 ** 3 = 8

🔹Example:
a = 10
b =3 
print(a+b)
print(a%b)
print(a**b)

24.Assignment Operator 

◽Assingment operator are used to aasign or update values of variables

Common Assignment Operators

Operator                    Meaning                   Example:

=                        Assign                        x = 10

+=                       Add and assign                x += 5
 
-=                       Subtract and assign           x -= 5

*=                       Muliply and assign            x *=  5

/=                       Divide and assign             x /= 5

%=                       Modulus and assign            x %= 5


🔹Example:

x = 10 
x += 5
print (x)


25. Camparison operator 

Camparision operator are used to campare two values. They return a Boolean values( True or False).

Operator                  Meaning                  Example
==                       Equal to                   10 == 10 ---> True
!=                       Not equal to               10 != 5  --->  True
>                        Greater than               10 > 5   --->   True
<                        Less  than                 10 < 5   --->    False
>=                       Greater than or equal to   10 >= 10 ---> True
<=                     

🔹Example:

a = 10 
b = 5

print(a > b)
print( a == b)

Output:
True
False


26.logical Operator 
◽Logical operator are used to combine or reverse condition . They return True or Fasle.

Types  


Operator                        Meaning

and                             True if both condition is true

or                              True is at least one condition is true

not                             Reverse the result


🔹Example:

a = 10
b = 5

print (a > 5 and b < 10)   # True
print (a > 15 and b < 10)  # True
print (not(a > 5))         #False

27.Bitwise Operator

◽Bitwise operators are used to perform operation on the binary bits (0 and 1) of numbers.

Types   
Operator                         Meaning
&                                 AND

`                                  `

^                                 XOR

~                                 NOT

<<                               Left Shift

>>                               Right Shift


🔹Example:

a = 5
b = 3

print(a & b)
print(a | b)


#Output
1
7

28. Membership Operators
◽ Membership operator are used to check whether a value exists in a sequence such as a list, tuple,string,or set

 Type

 Operator                      Meaning
 in                           Return True if the value is present

 not in                       Return True if the  value is not present


 
 🔹Example:

 fruits = ["Apple", "Mango", "Banana"]

 print("Mango" in fruits)
 print("Orange" not in fruits)

 Output:
 True
 True

 29.Identity Operators 
  
 Identity operators  are used to check whether two variables refer to the same objectin memory.

 TYPE

 Operator                     Meaning

 is                          Return True if both variables refer to the same object

 is not                      Returns True if they refer to diffrents object
   
#🔹Example:

a = [1,2,3]
b = a

print(a is b)
print(a is not b)

Output:
True
False

30.Difference Betwween ===  and is
 
 ==Operator

 Cheack whether two values are equal.

 is Operator

 Check whether two variables refer to the same object in memory.

 #🔹Example:

 a = [1, 2, 3]
 b = [1, 2, 3]

 print(a == b)
 print(a is b)

 Output:
 True
 False

Diffrence :

==Operator                                        is Operator
Check weather values are equal                    Checks whether both variables refer to the same object
Used for value  comparision                       Used for identity comparison
Example: a == b                                   Example: a is b
Commonly used in condition                        Commonly used to campare with None

31.Operator Precedence 

◽Operator precedence means the order in which operators are executed in an expression.

 #🔹Example:
result = 10 + 5 * 2
print(result)

Output:
20

Why?

*has higer precedence than +, so:
10 + (5 * 2)
= 10 + 10
20

--Common Precedence Order--

From  higher to lower
1.() --> Parenthesis 
2.** --> Exponentiation 
3.* ///% --> Multiplication,Division
4.+ -   --> Addition, Subtraction
5. == != > < >=  <= --> Comparison
6. not -->  Logical NOT
7.and --> logical AND
8.OR ---> logical OR

 #🔹Example:

result = 20 - 4 * 3 +  2
print(result) 
 
Output:
10

why?
First * is performed because multiplication has higher precedence:

20 - (4 * 3) + 2
= 20 - 12 + 2
= 10

Remember: * is performed before + and -.
         """ 
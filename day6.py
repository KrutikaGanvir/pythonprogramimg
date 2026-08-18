#-----SOLVE PRACTICE PROBLEMS--------

# 1. Add two numbers
'''
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

sum_value = a + b
print("Sum =",sum_value)
'''

# 2.Calculate aarea of reactangle
'''
length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))

area = length * breadth
print("Area of reactangle =", area)
 '''

# 3.Caculate simple interest
'''
principal  = float(input("Enter principle amount:"))
rate = float(input("Enter rate:"))
time = float(input("Enter time:"))

simple_interest =(principal * rate * time) / 100
print("Simple Interest =", simple_interest)
'''


#4.Swap two numbers
'''
a = 10
b = 20

a,b = b,a
print("a=",a)
print("b=",b)
'''

# 5.Check type of user input

value = input("Enter any value:")
print("Value:",value)
print("Type:",type(value))
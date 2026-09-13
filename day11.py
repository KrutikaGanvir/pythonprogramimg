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


    '''

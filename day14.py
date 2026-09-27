'''-------------------------PRACTICE PROBLEMS-------------------------------------


1. Reverse a String



text = input("Enter a string:")

reverse = text[:: - 1]

print("Reverse string =", reverse)


2.Palindrome String

A palindrome string is a string that reads the same forword and backword.

example: madam --> madam


text = input("Enter a string:")

if text == text[:: -1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")



3. Count Vowels


text = input ("Enter a string:")

count = 0

for char in text:
    if char.lower() in "aeiou":
        count = count + 1
        print("Number of vowels =", count)



4 Take a name from user and print its length.        

     

name = input("Enter your name:")
print ("length of name = ", len(name))


◽Logic: 

 len() function counts the number of character in a string.



5. Reverse a string without using slicing.
 

text = input ("Enter a string:")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reverse string =", reverse)


    
6. Count vowels and consonants.  
     
text = input("Enter a string:")

vowels = 0
consonants = 0

for char in text:
    if char . lower() in "aeiou":
        vowels = vowels + 1

    elif char.isalpha():
        consonants = consonants + 1
print("Vowels =" , vowels)
print("Consonants =" , consonants)


◽Logic: 

🔹aeiou --> Vowels
🔹Other alphabets ---> Consonents
🔹isalpha() ignores spaces, numbers, and symbols

 '''
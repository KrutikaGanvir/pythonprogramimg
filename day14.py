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

        '''
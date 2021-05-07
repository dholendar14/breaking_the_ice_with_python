"""
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3  
"""
letter = 0
number = 0
l = input().split(" ")
for i in l:
    for j in i:
        if j.isalpha():
            letter = letter + 1
        elif j.isdigit():
            number = number + 1
print("LETTER {} \nDIGITS {} ".format(letter,number))

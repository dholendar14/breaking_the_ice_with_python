"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9 """

upper = 0
lower = 0
l = input().split()
for i in l:
    for j in i:
        if j.isupper():
            upper = upper + 1
        elif j.islower():
            lower = lower + 1
print("UPPER CASE {} \nLOWER CASE {}".format(upper,lower))
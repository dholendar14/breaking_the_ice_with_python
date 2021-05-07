""" Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106 """

num = input()
tota1 = int(num) + int(num * 2) + int(num * 3) + int(num * 4)
print(tota1)
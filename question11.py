'''    Write a program, which will find all such numbers between 1000 and 3000 (both included) 
    such that each digit of the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.'''
lst = []
for i in range(2000,3001):
    flag = 0
    for n in str(i):
        if int(n)%2 == 0:
            flag = flag + 1
    if flag == 4:
        lst.append(str(i))

print(",".join(lst))
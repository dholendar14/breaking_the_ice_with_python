""" Write a program that computes the net amount of a bank account based a transaction log 
    from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500 """


total = 0
while True:
    x = input()
    w = []
    if len(x) == 0:
        break
    w = x.split(" ")
    for item in w:
        if(item.lower() == 'd'):
            total += int(w[1])
        elif(item.lower() == 'w'):
            total -= int(w[1])
print(total)

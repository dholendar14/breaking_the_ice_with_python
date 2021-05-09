import time
import random
from operator import add,mul,sub

score = 0
start_time = time.time()
operators = {
    "+": add,
    "-": sub,
    "*": mul
}
keys = list(operators)
operator = random.choice(keys)
while time.time() - start_time <= 60:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    oper = random.choice(keys)
    answer = int(input("{} {} {} \n".format(num1,oper,num2)))
    if answer == (operators[operator](num1,num2)):
        score += 1
        print("Correct! Time remain {} seconds".format(int(60 -(time.time() - start_time))))
    else:
        print("Wrong! Time remain {} seconds".format(int(60 -(time.time() - start_time))))
print("you have scored: {}".format(score))
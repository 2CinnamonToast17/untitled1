'''
Step 1: Increase answer by 10
Step 2: Divide Answer by each number below 11
*if all numbers below 11 go into answer wholly
Conditions are met and answer is found'''

import time

answer = 20 #must be one because it passes thru if statement in line 16

def divCheck(num):
    for i in range(10, 21):
        if num % i == 0:
            #print(num, 'Is Divisible by', i)
            continue
        else:
            return False
    return True
t0 =time.time()

while not divCheck(answer):
    answer += 20

print(answer)
t1 = time.time()

total = t1-t0
print(total)


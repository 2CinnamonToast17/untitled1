                    #Find the 10001st prime number
import time
import math


def isPrime(num):
    if num == 1:
        return False
    elif num < 4:
        return True
    elif num % 2 == 0:
        return False
    elif num < 9:
        return True
    elif num % 3 == 0:
        return False

    else:
        r = math.floor(math.sqrt(num))
        f = 5
        while f <= r:
            if num % f == 0:
                return False
            if num % (f+2) == 0:
                return False
            f += 6
        return True

count = 1
answer = 1

t0 = time.time()
while count != 10001:
    answer += 2
    if isPrime(answer):
        count += 1
print(answer)
t1 = time.time()

total = t1-t0
print(total)

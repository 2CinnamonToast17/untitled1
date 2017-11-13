result = 0
def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

# [::-1]

for a in range(2, 1000):
    for b in range(2, 1000):
        answer = a * b
        if is_palindrome(answer):
            if result < answer:         #Determines Largest Palindrome
                result = answer

print(result)




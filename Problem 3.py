
number = 600851475143


'''
while integer * integer < number:
    while number % integer == 0:            #checking if remainder is 0
        number /= integer                   #number = number/integer

    integer += 1
print(number)
'''

def greatestPrimeFactor(number):
    integer = 2
    while integer * integer < number:
        while number % integer == 0:
            number /= integer

        integer += 1

    return number

print(greatestPrimeFactor(number))
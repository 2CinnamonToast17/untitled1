

a, b = 1, 0
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b
print(total)






number = 600851475143
integer = 2


while integer * integer < number:
    while number % integer == 0:
        number = number / integer
    integer += 1

print(number)
print(integer)

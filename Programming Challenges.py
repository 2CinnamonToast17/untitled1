from fractions import Fraction

def workingWithNumbers():

    def evenOddVendingMachine(n):

        amount = 9
        count = 0
        if n % 2 == 0:
            print(n, 'is Even')
            print('These are the next 9 even numbers following', n)
        else:
            print(n, 'is odd')
            print('These are the next 9 odd numbers following', n)

        while count < amount * 2:
            count += 2
            print(n + count)


    def multiTable(n):

        for i in range(1, 16):                  # has to be x+1 or else does not compute x
            print(n, 'x', i, '=', n * i)


    def unitConversion():
        def massConversion(n):
            print('Enter 1 for Kilograms to Pounds...')
            print('Enter any other number for Pounds to Kilograms')
            if int(input()) == 1:
                answer = n * 2.2
                print(n, ' Kilograms is ', answer, ' Pounds')

            else:
                answer = n // 2.2
                print(n, ' Pounds is ', answer, ' Kilograms')


        def tempConversion(n):
            print('Enter 1 for Fahrenheit to Celsius...')
            print('Enter any other number for Celsius to Fahrenheit')
            if int(input()) == 1:
                answer = (n - 32) * (5 / 9)
                print(n, ' degrees Fahrenheit is ', answer, ' degrees Celsius')

            else:
                answer = n * (9 / 5) + 32
                print(n, ' degrees Celsius is ', answer, ' degrees Fahrenheit')

        if __name__ == '__main__':
            op = input('Would you like Temperature or a Mass conversion? - Temperature, Mass: ')
            if op == 'Temperature':
                a = int(input('What is the degree of the temperature? '))
                tempConversion(a)
            if op == 'Mass':
                a = int(input('What is the numerical value of the mass? '))
                massConversion(a)


    def fractions():
        def add(a, b):
            print('Result of Addition: {0}'.format(a + b))

        def subtract(a, b):
            print('Result of Subtraction: {0}'.format(a - b))

        def divison(a, b):
            print('Result of Division: {0}'.format(a / b))

        def multiply(a, b):
            print('Result of Multiplication: {0}'.format(a * b))

        if __name__ == '__main__':
            a = Fraction(input('Enter first fraction: '))
            b = Fraction(input('Enter second fraction: '))
            op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
            if op == 'Add':
                add(a, b)
            if op == 'Subtract':
                subtract(a, b)
            if op == 'Divide':
                divison(a, b)
            if op == 'Multiply':
                multiply(a, b)


    def exit():
        print('Thank you for using "Working with Numbers"')
        return None

    if __name__ == '__main__':
        op = input('Please choose: -Even or Odd Vending Machine, Multiplication Table, Unit Conversions, Fractions, Exit- ')
        if op == 'Even or Odd Vending Machine':
            a = int(input("What Number would you like to process? "))
            evenOddVendingMachine(a)
        if op == "Multiplication Table":
            a = int(input("What Number would you like to multiply? "))
            multiTable(a)
        if op == "Unit Conversions":
            unitConversion()
        if op == "Fractions":
            fractions()
        if op == "Exit":
            exit()

workingWithNumbers()

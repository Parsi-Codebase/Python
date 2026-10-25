# Handling specific Excpetions
try:
    number=int(input('Enter a number'))
    result=100/number
    print('Result',result)
except ValueError:
    print('Please enter a valid number')
except ZeroDivisionError:
    print('Number cannot be zero')
# finally executes when an exception occure or not
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Calculation successful")
    print("Result:", result)
finally:
    print("Finally block executed")
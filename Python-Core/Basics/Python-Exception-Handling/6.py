# else block
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
# else block not get execute when exception occure
else:
    print("Calculation successful")
    print("Result:", result)
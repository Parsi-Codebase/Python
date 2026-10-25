# try-except-else-finally
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Calculation successful")
    print("Result:", result)

finally:
    print("Program execution completed")
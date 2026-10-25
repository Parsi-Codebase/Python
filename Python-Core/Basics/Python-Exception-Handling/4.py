# multiple except blocks
try:
    value = int(input("Enter number: "))

    result = 100 / value

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception:
    print("Unexpected error")
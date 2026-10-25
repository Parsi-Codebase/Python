# same handling logic applies to multiple exceptions.
try:
    number = int(input("Enter number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input")
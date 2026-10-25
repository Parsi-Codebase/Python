#Exception Hierarchy
try:
    numbers = [10, 20, 30]
    print(numbers[10])

except LookupError:
    print("Lookup error occurred")
#IndexError is a subclass of LookupError, so it is caught.
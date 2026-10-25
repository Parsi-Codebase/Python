# raising exception explicitly using raise
try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Eligible")

except ValueError as ex:
    print("Error:", ex)
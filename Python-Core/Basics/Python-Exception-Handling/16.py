# Context Manager and with for clean up
try:
    with open("students.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found")
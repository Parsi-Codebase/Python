#Instead of manually closing files, Python’s with automatically handles it.
with open("example.txt", "r") as file:
    data = file.read()
    print(data)

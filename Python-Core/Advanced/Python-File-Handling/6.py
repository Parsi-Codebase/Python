#Writing and Reading Binary Files
# Writing binary
data = bytes("Python Binary Example", 'utf-8')
with open("binaryfile.bin", "wb") as file:
    file.write(data)

# Reading binary
with open("binaryfile.bin", "rb") as file:
    print(file.read())

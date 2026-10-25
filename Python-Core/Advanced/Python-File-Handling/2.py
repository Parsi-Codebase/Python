# reading data from the file
file = open("example.txt", "r")
content = file.read() # read all the lines
content=file.readline() # read one line
content=file.readlines() # read all the line in list form
print(content)

file.close()

#Accessing List Elements
students = ["Ravi", "Raj", "Priya", "Anil"]

print(students[0])
print(students[1])
print(students[2])
#Modifying a List
students[1] = "Rahul"

print(students)
#Adding Elements
students.append("Priya")
students.insert(1, "Anil") #Adds an element at a specific position.
students.extend(["Priya", "Anil"]) #Adds multiple elements.
print(students)
#Removing Elements
students.remove("Raj")

print(students)
students.pop(1) #Removes an element using its index.

print(students)
del students[0]

print(students)

students.clear() # clear all items

print(students)
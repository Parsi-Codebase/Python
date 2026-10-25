# Creating a hash table using dict
student_info = {
    "roll_101": "Akhil",
    "roll_102": "Siri",
    "roll_103": "Shripad"
}
# Accessing value
name:str=student_info["roll_102"] # Accessing value for key "roll_102"
print(name)  # Output: Siri
print(student_info["roll_101"])  # Output: Akhil
# Adding a new entry
student_info["roll_104"] = "Ravi"
# Updating an existing value
student_info["roll_103"] = "Kiran R"
# Deleting a key
del student_info["roll_102"]
# Iterating over keys and values
for roll, name in student_info.items():
    print(roll, ":", name)

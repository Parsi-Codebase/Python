import os
#Checking File Existence and Deletion
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted!")
else:
    print("File does not exist.")

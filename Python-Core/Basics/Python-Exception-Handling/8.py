# finally commonly used for cleanup operations
file = None

try:
    file = open("data.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
# file should be closed even if an exceptio occurs
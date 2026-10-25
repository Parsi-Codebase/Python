thislist = ["apple", "banana", "cherry"]
# change item value
thislist[1] = "blackcurrant"
print(thislist)
# chage of range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist.append("orange")
print(thislist)
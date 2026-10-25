thislist = ["apple", "banana", "cherry"]
# remove item from the list
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
#Remove the first occurance of "banana":
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
# Remove Specified Index
thislist.pop(1)
print(thislist)
thislist = ["apple", "banana", "cherry"]
# Remove the last item
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
# The del keyword also removes the specified index:
del thislist[0]
print(thislist)
# to delete the list completely
thislist = ["apple", "banana", "cherry"]
del thislist
thislist = ["apple", "banana", "cherry"]
thislist.clear() # to clear the list
print(thislist)
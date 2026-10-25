
thislist = ["apple", "banana", "cherry"]
# access list items 
print(thislist[1])
# -1 refers to the last item, 
#-2 refers to the second last item etc.
print(thislist[-1])
# List slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4]) # from 0 to upto 4
print(thislist[2:]) # from 2 to end
print(thislist[-4:-1]) # from orange to melon
#Check if "apple" is present in the list
if 'apple' in thislist:
    print('Apple exisit in the list')
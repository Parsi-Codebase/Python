x = ("apple", "banana", "cherry")
y = list(x) # convert to list
y[1] = "kiwi"
x = tuple(y) # convert list ot tuple

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y  # add tuple to tuple

print(thistuple)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits # unpacking a tuple

print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # assigning the rest of the values
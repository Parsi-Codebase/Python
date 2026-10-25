numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
numbers.update([30, 40, 50])
print(numbers)
numbers.remove(20)
print(numbers)
numbers.discard(150) #discard() does not raise an error if the value doesn't exist.
print(numbers)
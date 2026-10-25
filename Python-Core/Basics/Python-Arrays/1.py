cars = ["Ford", "Volvo", "BMW"]
# access elements
print(cars[0])
print('No of Elements ',len(cars))
# adding array elments
cars.append('Benz')
for x in cars:
    print(x)
# remove array elements
print()
cars.pop()
#cars.pop(1) # delete the second element
#cars.remove('Volvo')
for x in cars:
    print(x)
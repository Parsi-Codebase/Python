# Exception object using as
try:
  number=10/0
except ZeroDivisionError as ex:
  print('Error:',ex)
  
# ex2
try:
    number = int("abc")

except ValueError as ex:
    print("Exception type:", type(ex).__name__)
    print("Message:", ex)
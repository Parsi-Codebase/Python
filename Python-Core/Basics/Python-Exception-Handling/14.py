#Exception Handling with Functions
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
result=divide(10,0)
if result is None:
    print('Division failed')
else:
    print(result)
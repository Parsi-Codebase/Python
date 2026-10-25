#Re-raising an Exception
def process():

    try:
        result = 10 / 0

    except ZeroDivisionError as ex:
        print("Logging error:", ex)
        raise
try:
    process()

except ZeroDivisionError:
    print("Exception handled by caller")
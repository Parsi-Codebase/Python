import datetime
x=datetime.datetime(2000,11,12)
#formatting date objects into readable strings
print(x.strftime('%a')) # weekday short version
print(x.strftime('%A')) # weekday long version
print(x.strftime('%b')) # month name short version
print(x.strftime('%B')) # month name full version
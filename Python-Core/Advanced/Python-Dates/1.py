import datetime

current = datetime.datetime.now()
print(current)
today = datetime.date.today() # getting only date
print(today)
my_birthday = datetime.date(1990, 12, 25) # creating specific date
print(my_birthday)
now = datetime.datetime.now()
#Getting Individual Components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Date Formating
print(now.strftime("%A, %d %B %Y"))   # Tuesday, 21 October 2025
print(now.strftime("%m/%d/%Y"))       # 10/21/2025
print(now.strftime("%I:%M %p"))       # 01:15 PM

#Parsing String to Date (strptime())

date_string = "21/10/2025 14:30"
date_obj = datetime.strptime(date_string, "%d/%m/%Y %H:%M")

print(date_obj)
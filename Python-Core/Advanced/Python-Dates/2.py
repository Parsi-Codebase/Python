from datetime import date,datetime, timedelta
# Date Arithmetic (Add/Subtract Dates)
today = datetime.now()
next_week = today + timedelta(days=7)
yesterday = today - timedelta(days=1)

print("Today:", today)
print("Next week:", next_week)
print("Yesterday:", yesterday)
#Difference Between Two Dates
d1 = date(2025, 10, 21)
d2 = date(2024, 10, 21)

diff = d1 - d2
print(diff.days, "days")

# working with time
from datetime import time

t = time(14, 30, 45)
print(t)
print("Hour:", t.hour)
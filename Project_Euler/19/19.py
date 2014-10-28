import datetime

count = 0
date = datetime.date(1901,1,1)
while True:
    if date.year == 2001:
        break
    if date.day == 1:
        if date.weekday() == 6:
            count += 1
    date += datetime.timedelta(days = 1)
print count

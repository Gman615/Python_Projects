from datetime import datetime, timedelta
from pytz import timezone




def todayAt(hr, min =0, sec=0, micros=0):
    now = datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

print(todayAt(17), todayAt(17, 15))

timeNow = datetime.now()
if timeNow < todayAt(13):
    print("Too Early")
else:
    print("Too Late")
print(timeNow)

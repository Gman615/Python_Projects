from datetime import datetime, timedelta





openTime = datetime.strptime('09:00AM', '%I:%M%p')
closeTime = datetime.strptime('05:00PM', '%I:%M%p')
time = '%I:%M%p'
time_here = datetime.now()
time_LA = datetime.now()
time_NYC = datetime.now()
time_London = datetime.now()

timezones = ['America/Los_Angeles', 'America/New_York_City', 'Europe/London']

def todayAt(hr, min =0, sec=0, micros=0):
    now = datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


if time_LA < todayAt(10) or time_LA > todayAt(18):
    print("The Portland office is closed")
else:
    print("The Portland office is open")

if time_NYC < todayAt(7) or time_NYC > todayAt(15):
    print("The New York City branch is closed")
else:
    print("The New York City branch is open")

if time_London < todayAt(2) or time_London > todayAt(10):
    print("The London branch is closed")
else:
    print("The London branch is open")





    

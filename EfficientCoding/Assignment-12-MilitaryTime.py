# with library
from datetime import datetime as dt
#print(dt.strptime(dt.strptime(input(), '%I%M%S%p'), '%H%M%S'))
tme = "11:21:30PM"
print(dt.strftime(dt.strptime(tme, '%I:%M:%S%p'), '%H:%M:%S'))


# without any library
tme = "11:21:30PM"
#hour, minutes, secondsplus = input().split(":")
hour, minutes, secondsplus = tme.split(":")
seconds, day = secondsplus[:-2], secondsplus[-2:]

if day == "AM" and hour == "12":
    hour = "00"

if day == "PM" and int(hour) < 12:
    hour = int(hour) + 12

print("{}:{}:{}".format(hour, minutes, seconds))

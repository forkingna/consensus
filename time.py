import time
dt = "2016-05-05 21:28:55"
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
timestamp = time.mktime(timeArray)
print(timestamp)
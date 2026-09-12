import datetime

currentDate = datetime.datetime.now()

print("Current date & time : ", end="")
print(currentDate.strftime("%Y-%m-%d %H:%M:%S"))
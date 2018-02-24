import time
import import_calendar

currentYear = int(time.strftime("%Y"))
currentMonth = int(time.strftime("%m"))
currentDay =int(time.strftime("%d"))
print(str(currentYear) +" " +str(currentMonth)+ " "+str(currentDay))

arrayYear = currentYear- import_calendar.creationYear
arrayMonth = currentMonth - 1
arrayDay = currentDay - 1

day_range = 7

for i in range(arrayDay, arrayDay+7):
    print( str(i+1))
    print(import_calendar.years[arrayYear][arrayMonth][i])
    

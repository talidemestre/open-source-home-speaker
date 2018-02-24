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

if (day_range + arrayDay <= len(import_calendar.years[arrayYear][arrayMonth])):
    for i in range(arrayDay, arrayDay+day_range):
        print( str(arrayMonth) +" " +  str(i+1))
        print(import_calendar.years[arrayYear][arrayMonth][i])
else:
    for i in range(arrayDay, arrayDay + (len(import_calendar.years[arrayYear][arrayMonth]) - arrayDay)):
        print( str(arrayMonth) +" " +  str(i+1))
        print(import_calendar.years[arrayYear][arrayMonth][i])


        
    for i in range(0, day_range - (len(import_calendar.years[arrayYear][arrayMonth]) - arrayDay)):
        print( str(arrayMonth+1) +" " +  str(i+1))
        print(import_calendar.years[arrayYear][arrayMonth + 1][i])

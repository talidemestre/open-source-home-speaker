import time

#Generating a blank calendar
currentYear = int(time.strftime("%Y"))
years=[]
#creates intial year array
for i in range(currentYear, currentYear+10):
    years.append([])    
year = currentYear
#populates the years with days and months
for x in years:    
    for i in range(0,12):        
        if (i != 8) and (i != 3) and (i != 5) and (i != 9)and (i != 1):
            x.append(['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
        elif (i == 1):
            #checks if the year is a leap year
            if (year%400==0) or (year%4 == 0) and (year%100!=0):
                x.append(['','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
            else:
                x.append(['','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
        else:
            x.append(['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
    #increases year count for leap year checking
    year+=1


#writes data to external files
write_data = open('import_calendar.py', 'w')
write_data.write("creationYear=" + str(currentYear) + "\nyears =" + str(years))
write_data.close()


write_data = open('import_alarms.py', 'w')
write_data.write("alarms_list=[]")
write_data.close()

write_data = open('import_perma_alarms.py', 'w')
write_data.write("alarms_list=[]")
write_data.close()

write_data = open('import_lists.py', 'w')
write_data.write("lists=[['notes']]")
write_data.close()

years=[]
#creates intial year array
for i in range(2018, 2028):
    years.append([])    
year = 2018
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

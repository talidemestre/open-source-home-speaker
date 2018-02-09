import time
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



testDate = "set the date feed the baby for twenty third march twenty eighteen"
testDate = testDate.split(' ')
FinalMonth = 12
FinalDay=32
FinalYear=2000

print (testDate)

dayList = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth']
monthList = ['january',  'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october','november','december']

prefix =['twenty', 'two']
midfix ='thousand'
daySuffix = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
yearSuffix = [ 'eighteenth', 'nineteenth', 'twenty']


for word in range(0, len(testDate)):
    for month in range(0, len(monthList)):
        if testDate[word] == monthList[month]:
            FinalMonth = month
    for day in range(0, len(dayList)):
        if testDate[word] == dayList[day]:
            FinalDay = day
    for 
    

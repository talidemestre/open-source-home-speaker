import time
import import_calendar
import importlib

importlib.reload(import_calendar)

UserVoiceInput= "set event brush teeth for the thirtieth may two thousand eighteen"

testDate = UserVoiceInput.split(' ')
finalMonth = int(time.strftime("%m"))
finalDay=int(time.strftime("%d"))+1
finalYear=int(time.strftime("%Y"))
#print (testDate)


###ADD THIRTIETH
daySpecialCase ="thirtieth"

dayList = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth']
monthList = ['january',  'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october','november','december']




#prefixes/suffixes to be checked to determine the day/date using an iterable string
prefix =['twenty', 'two']
midfix ='thousand'

daySuffix = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
yearSuffix = [ 'eighteen', 'nineteen', 'twenty']

#iterating through the string and matching against words in the previous strings to determine the requested date
for word in range(0, len(testDate)):
    for month in range(0, len(monthList)):
        if testDate[word] == monthList[month]:
            finalMonth = month
    for day in range(0, len(dayList)):
        if testDate[word] == dayList[day] and testDate[word-1] != 'twenty' and testDate[word-1] != 'thirty' and testDate[word-1] != 'thousand':
            finalDay = day
    if testDate[word] == 'thirtieth':
        finalDay = 29
    if testDate[word] == 'twenty':
        for y in range(0, len(yearSuffix)):
            if testDate[word+1] == yearSuffix[y]:
                finalYear == yearSuffix[y] + import_calendar.creationYear
        for z in range(0, len(daySuffix)):
            if testDate[word+1] == daySuffix[z]:
                finalDay= z + 20
    if testDate[word] == 'thirty':
        print("found")
        for y in range(0, len(yearSuffix)):
            if testDate[word+1] == yearSuffix[y]:
                finalYear == yearSuffix[y] + import_calendar.creationYear
        for z in range(0, len(daySuffix)):
            if testDate[word+1] == daySuffix[z]:
                print("made it")
                finalDay= z + 30
    if testDate[word] == 'two':
        if testDate[word+1] == 'thousand':
            for y in range(0, len(yearSuffix)):
                if testDate[word+1] == yearSuffix[y]:
                    finalYear == yearSuffix[y] + import_calendar.creationYear

#print(finalDay, finalMonth, finalYear)
#writing results to the file that stores the calendar
import_calendar.years[finalYear - int(time.strftime("%Y"))][finalMonth][finalDay] = UserVoiceInput
write_data = open('import_calendar.py', 'w')
write_data.write("creationYear=" + str(import_calendar.creationYear) + "\nyears =" + str(import_calendar.years))
write_data.close()


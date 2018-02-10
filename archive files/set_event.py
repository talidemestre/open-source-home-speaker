
def SetEvent(UserVoiceInput):
    testDate = UserVoiceInput.split(' ')
    finalMonth = int(time.strftime("%M"))
    finalDay=32
    finalYear=int(time.strftime("%Y"))
    #print (testDate)

    dayList = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth']
    monthList = ['january',  'february', 'march', 'april', 'may', 'june', 'july', 'august','september', 'october','november','december']

    prefix =['twenty', 'two']
    midfix ='thousand'
    daySuffix = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth']
    yearSuffix = [ 'eighteenth', 'nineteenth', 'twenty']
    for word in range(0, len(testDate)):
        for month in range(0, len(monthList)):
            if testDate[word] == monthList[month]:
                finalMonth = month
        for day in range(0, len(dayList)):
            if testDate[word] == dayList[day]:
                finalDay = day
        if testDate[word] == 'twenty':
            for y in range(0, len(yearSuffix)):
                if testDate[word+1] == yearSuffix[y]:
                    finalYear == yearSuffix[y] + 2018
            for z in range(0, len(daySuffix)):
                if testDate[word+1] == daySuffix[z]:
                    finalDay= z + 20
        if testDate[word] == 'two':
            if testDate[word+1] == 'thousand':
                for y in range(0, len(yearSuffix)):
                    if testDate[word+1] == yearSuffix[y]:
                        finalYear == yearSuffix[y] + 2018

    print(finalDay, finalMonth, finalYear)
    years[finalYear - int(time.strftime("%Y"))][finalMonth][finalDay] = UserVoiceInput
        



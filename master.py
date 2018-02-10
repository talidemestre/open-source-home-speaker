import pypygo
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



#UserVoiceInput = "Hey google, set an alarm for four thirty"
UserVoiceInput = input() #placeholder voice-interpreted text
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable

#print (VoiceArray) ##DEBUG LINE

##--Trigger Words For Each Command--##
CommandOneWords = ["play", "music", "song"]
CommandTwoWords = ["set", "alarm", "timer"]
CommandThreeWords = ["set", "calendar", "event","date","schedule"]
CommandFourWords = ["whats", "on", "schedule"]
CommandFiveWords = ["take", "write", "note"]
CommandSixWords = ["make", "list", "create"]
CommandSevenWords = ["add", "list", "write",]

##--Total Matched Words with Trigger Words--##
CommandOneCount = 0
CommandTwoCount = 0
CommandThreeCount = 0
CommandFourCount = 0
CommandFiveCount = 0
CommandSixCount = 0
CommandSevenCount = 0

##--Placeholder Functions For Each Function--##
def Command1(UserVoiceInput):
        print ("Attempting to play music...")
def Command2(UserVoiceInput):
        print ("Attempting to set alarm...")
def Command3(UserVoiceInput):
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
            if testDate[word] == dayList[day] and testDate[word-1] != 'twenty' and testDate[word-1] != 'thousand':
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
        





def Command4(UserVoiceInput):
        print ("Attempting to gather schedule...")
def Command5(UserVoiceInput):
        print ("Attempting to write note...")
def Command6(UserVoiceInput):
        print ("Attempting to add to list...")
def Command7(UserVoiceInput):
        print ("Attempting to create list...")
        
def Search (UserVoiceInput):
        print("I ran a search for " + UserVoiceInput +":")
        search=pypygo.query(UserVoiceInput)
        print(search.abstract)

##--Word Matching--##
for i in range (0, len(VoiceArray)):
    for x in range (0, len(CommandOneWords)):
        if VoiceArray[i] == CommandOneWords[x]:
            CommandOneCount+=1
    for x in range (0, len(CommandTwoWords)):
        if VoiceArray[i] == CommandTwoWords[x]:
            CommandTwoCount+=1
    for x in range (0, len(CommandThreeWords)):
        if VoiceArray[i] == CommandThreeWords[x]:
            CommandThreeCount+=1
    for x in range (0, len(CommandFourWords)):
        if VoiceArray[i] == CommandFourWords[x]:
            CommandFourCount+=1
    for x in range (0, len(CommandFiveWords)):
        if VoiceArray[i] == CommandFiveWords[x]:
            CommandFiveCount+=1
    for x in range (0, len(CommandSixWords)):
        if VoiceArray[i] == CommandSixWords[x]:
            CommandSixCount+=1
    for x in range (0, len(CommandSevenWords)):
        if VoiceArray[i] == CommandSevenWords[x]:
            CommandSevenCount+=1


##--Command with most matches is called--##
Counts = [CommandSevenCount,CommandSixCount,CommandFiveCount,CommandFourCount,CommandThreeCount,CommandTwoCount,CommandOneCount]

Maximum=max(Counts)
if Maximum == 0:
        Search(UserVoiceInput)
elif CommandOneCount== Maximum:
    Command1(UserVoiceInput)
elif CommandTwoCount== Maximum:
    Command2(UserVoiceInput)
elif CommandThreeCount== Maximum:
    Command3(UserVoiceInput)
elif CommandFourCount== Maximum:
    Command4(UserVoiceInput)
elif CommandFiveCount== Maximum:
    Command5(UserVoiceInput)
elif CommandSixCount== Maximum:
    Command6(UserVoiceInput)
elif CommandSevenCount== Maximum:
    Command7(UserVoiceInput)
else:
        Search(UserVoiceInput)
        
        

import pypygo
import time
import import_calendar
import importlib
import import_alarms
import import_perma_alarms
##--Trigger Words For Each Command--##
CommandOneWords = ["play", "music", "song"]
CommandTwoWords = ["set", "alarm", "timer"]
CommandThreeWords = ["set", "calendar", "event","date","schedule"]
CommandFourWords = ["whats", "on", "schedule", "calendar"]
CommandFiveWords = ["take", "write", "note"]
CommandSixWords = ["make", "list", "create"]
CommandSevenWords = ["add", "list", "write"]
CommandEightWords = ["cancel", "alarm", "music", "stop", "pause","cease","end","terminate","conclude","finish","desist"]


##--Placeholder Functions For Each Function--##
def Command1(UserVoiceInput):
        print ("Attempting to play music...")
def Command2(UserVoiceInput):
        importlib.reload(import_alarms)
        importlib.reload(import_perma_alarms)

        hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

        minuteMono = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        minutePrefix =['twenty','thirty','fourty','fifty']
        minuteSuffix =['one', 'two', 'three', 'four', 'five', "six", "seven", "eight", "nine"]

        finalHour=0
        finalMinute=0

        AMorPM = "PM" ###DEFAULT PLEASE CHANGE###

        hour_detected = False

        permanent=False

        
        for word in range(0, len(VoiceArray)):
            print (VoiceArray[word])
            if VoiceArray[word] == 'permanent' or VoiceArray[word]=='perma':
                permanent = True
            if VoiceArray[word] == 'am':#
                AMorPM ="AM"#
            if VoiceArray[word] == 'pm':#The voice detection will likely not read these as AM or PM and as such they should be updated.
                AMorPM ="PM" #               
            if hour_detected == False:
                for i in range (0, len(hourList)):
                    if VoiceArray[word] == hourList[i]:
                        hour_detected = True
                        finalHour = i+1              
            else:
                for i in range (0, len(minutePrefix)):
                    if VoiceArray[word] == minutePrefix[i]:
                        finalMinute+= 10*((i+2))
                for i in range (0, len(minuteSuffix)):
                    if VoiceArray[word] == minuteSuffix[i]:
                        finalMinute += i+1
                for i in range (0, len(minuteMono)):
                    if VoiceArray[word] == minuteMono[i]:
                        finalMinute = i + 10

        alarm= [finalHour, finalMinute, AMorPM]

        import_alarms.alarms_list.append(alarm)

        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()

        if permanent == True:
                import_perma_alarms.alarms_list.append(alarm)
                write_data = open('import_perma_alarms.py', 'w')
                write_data.write("alarms_list=" + str(import_perma_alarms.alarms_list))
                write_data.close()
#COMMAND THAT SETS DATES        
def Command3(UserVoiceInput):
        importlib.reload(import_calendar)

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

##COMMAND THAT GATHERS EVENTS ON CALENDAR        
def Command4(UserVoiceInput):
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
        
def Command5(UserVoiceInput):
        print ("Attempting to write note...")
def Command6(UserVoiceInput):
        print ("Attempting to add to list...")
def Command7(UserVoiceInput):
        print ("Attempting to create list...")
def Command8(UserVoiceInput):
        importlib.reload(import_alarms)
        currentHour=int(time.strftime("%I"))
        currentMinute=int(time.strftime("%M"))
        currentFormat=time.strftime("%p")
        
        print(time.strftime("%I"))
        print(time.strftime("%M"))
        print(time.strftime("%p"))

        
        for i in (0, len(import_alarms.alarms_list)-1):
            if import_alarms.alarms_list[i][0] == currentHour:
                if import_alarms.alarms_list[i][1] == currentMinute:
                    if import_alarms.alarms_list[i][2] == currentFormat:
                         import_alarms.alarms_list.remove([currentHour, currentMinute, currentFormat])


        print([currentHour, currentMinute, currentFormat])
        print (import_alarms.alarms_list)                         
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()
        
def Search (UserVoiceInput):
        print("I ran a search for " + UserVoiceInput +":")
        search=pypygo.query(UserVoiceInput)
        print(search.abstract)
while True:
        ##--Total Matched Words with Trigger Words--##
        CommandOneCount = 0
        CommandTwoCount = 0
        CommandThreeCount = 0
        CommandFourCount = 0
        CommandFiveCount = 0
        CommandSixCount = 0
        CommandSevenCount = 0
        CommandEightCount = 0

        #UserVoiceInput = "Hey google, set an alarm for four thirty"
        UserVoiceInput = input() #placeholder voice-interpreted text
        UserVoiceInput = UserVoiceInput.lower()
        VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable

        #print (VoiceArray) ##DEBUG LINE

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
            for x in range (0, len(CommandEightWords)):
                if VoiceArray[i] == CommandEightWords[x]:
                    CommandEightCount+=1


        ##--Command with most matches is called--##
        Counts = [CommandEightCount,CommandSevenCount,CommandSixCount,CommandFiveCount,CommandFourCount,CommandThreeCount,CommandTwoCount,CommandOneCount]

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
        elif CommandEightCount== Maximum:
            Command8(UserVoiceInput)
        else:
                Search(UserVoiceInput)
        
        

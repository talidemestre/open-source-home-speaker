import pypygo
import time
import import_calendar
import importlib
import import_alarms
import import_perma_alarms
import import_lists

#music search
import pafy
import vlc
import urllib.request
import urllib.parse
import re

#speech to text
import speech_recognition as sr
r = sr.Recognizer()
WIT_AI_KEY = "JL4IADZ4ODXSZ6RARKDP3IMMO66OSPS6"

#text to speech
import pyttsx3
engine = pyttsx3.init()



##--Trigger Words For Each Command--##
CommandOneWords = ["play", "music", "song"]
CommandTwoWords = ["set", "alarm", "timer"]
CommandThreeWords = ["set", "calendar", "event","date","schedule"]
CommandFourWords = ["whats", "on", "schedule", "calendar"]
CommandFiveWords = ["take", "write", "note"]
CommandSixWords = ["make", "list", "create", "named", "called", "titled"]
CommandSevenWords = ["add", "to", "list", "write"]
CommandEightWords = ["cancel", "alarm", "music", "stop", "cease","end","terminate","conclude","finish","desist"]
CommandNineWords = ["pause", "unpause", "music", "Stop", "song"]

#initialize player here, so music doesnt stack
Instance = vlc.Instance()
global player
player = Instance.media_player_new()


##--Core Functions--##
def DisplayAndSay(text):
        print(text)
        engine.say(text)        #vocalizes and displays the text
        engine.runAndWait()

##--Command Functions--##
def Command1(UserVoiceInput):
        player.stop() #stops any currently palying tracks before starting a new one
        search_term= ''
        found_song = False

        #extracts everything after either the first 'play' or first 'song'
        for i in VoiceArray:
            if found_song == True:
                search_term = search_term +' ' + i
            else:
                if i == 'song' or i =='play':
                    found_song = True


        #searches for user song, credit of Grant Curell https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
        query_string = urllib.parse.urlencode({"search_query" : search_term + 'song'}) #'song' added to end to lower chance of non-song results
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        url = "http://www.youtube.com/watch?v=" + search_results[0]

        print(url)

        #extracts audio from selected song's youtbe video
        video = pafy.new(url)
        best = video.getbestaudio()
        playurl = best.url


        #plays selected song in vlc
        Instance = vlc.Instance()
        global player
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        DisplayAndSay("Playing " + video.title + ".")
        player.play()

def Command2(UserVoiceInput):
        importlib.reload(import_alarms)
        importlib.reload(import_perma_alarms)

        hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

        minuteMono = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        minutePrefix =['twenty','thirty','forty','fifty']
        minuteSuffix =['one', 'two', 'three', 'four', 'five', "six", "seven", "eight", "nine"]

        finalHour=0
        finalMinute=0

        AMorPM = "PM" ###DEFAULT PLEASE CHANGE###

        hour_detected = False

        permanent=False

        
        for word in range(0, len(VoiceArray)):
            print (VoiceArray[word])
            #determine if alarm is to be permanent or one-time
            if VoiceArray[word] == 'permanent' or VoiceArray[word]=='perma':
                permanent = True
            #checks if AM or PM time
            if VoiceArray[word] == 'am':
                AMorPM ="AM"
            if VoiceArray[word] == 'pm':
                AMorPM ="PM"
            #if hour word is not found set hour, otherwise search for minutes
            if hour_detected == False:
                for i in range (0, len(hourList)):
                    if VoiceArray[word] == hourList[i]:
                        hour_detected = True
                        finalHour = i+1              
            else:
                for i in range (0, len(minutePrefix)):
                    if VoiceArray[word] == minutePrefix[i]: #find prefix for minute, e.g. twenty,thirty,fifty
                        finalMinute+= 10*((i+2))
                for i in range (0, len(minuteSuffix)):
                    if VoiceArray[word] == minuteSuffix[i]: #find suffix of minute, e.g. one, two, nine
                        finalMinute += i+1
                for i in range (0, len(minuteMono)):
                    if VoiceArray[word] == minuteMono[i]: #find a mono minute, e.g. ten, twelve, nineteen
                        finalMinute = i + 10

        alarm= [finalHour, finalMinute, AMorPM]

        import_alarms.alarms_list.append(alarm)

        
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()

        #add (or dont) to permanent alarm list
        if permanent == True:
                import_perma_alarms.alarms_list.append(alarm)
                write_data = open('import_perma_alarms.py', 'w')
                write_data.write("alarms_list=" + str(import_perma_alarms.alarms_list))
                write_data.close()
                DisplayAndSay("Permanent alarm set for " + str(finalHour) + " " + str(finalMinute) + " " + str(AMorPM))
        else:
                DisplayAndSay("Alarm set for " + str(finalHour) + " " + str(finalMinute) + " " + str(AMorPM))
#COMMAND THAT SETS DATES        
def Command3(UserVoiceInput):
        importlib.reload(import_calendar)

        testDate = UserVoiceInput.split(' ')
        finalMonth = int(time.strftime("%m"))
        finalDay=int(time.strftime("%d"))+1
        finalYear=int(time.strftime("%Y"))


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
        DisplayAndSay("Event set for " + str(finalDay+1) + " " + monthList[finalMonth] + " " + str(finalYear))

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
                DisplayAndSay(import_calendar.years[arrayYear][arrayMonth][i])
        else:
            for i in range(arrayDay, arrayDay + (len(import_calendar.years[arrayYear][arrayMonth]) - arrayDay)):
                print( str(arrayMonth) +" " +  str(i+1))
                DisplayAndSay(import_calendar.years[arrayYear][arrayMonth][i])


                
            for i in range(0, day_range - (len(import_calendar.years[arrayYear][arrayMonth]) - arrayDay)):
                print( str(arrayMonth+1) +" " +  str(i+1))
                DisplayAndSay(import_calendar.years[arrayYear][arrayMonth + 1][i])
        
def Command5(UserVoiceInput):
        importlib.reload(import_lists)
        string_add=''

        note_found=False

        for i in VoiceArray:
            if note_found == True:
                string_add = string_add + " " + i
            if i == 'note':
                note_found = True

        import_lists.lists[0].append(string_add)
        write_data = open('import_lists.py', 'w')
        write_data.write("lists=" +str(import_lists.lists))
        write_data.close()
        DisplayAndSay("Note: '" + string_add + "', added to list.")
def Command6(UserVoiceInput):
        importlib.reload(import_lists)
        synonyms = ["list", "named", "called", "titled", "dubbed", "labelled", "termed", "christened", "denominated", "termed", "styled", "identified", "entititled", "termed"] #these are all synonyms for 'named' so that the program can determine what to name the list
        title_after=0 #position of last word before title, default


        title = 'list' #default title


        #searching for synonym of 'named'
        for i in range(0, len(VoiceArray)):
            for x in synonyms:
                if VoiceArray[i] == x:
                    title_after = i



        #allocating title
        title = VoiceArray[title_after + 1]

        new_list = [title]

        dupe_found = False#tests if title is duplicate of existing title
        for i in import_lists.lists:
                if i[0] == title:
                        dupe_found = True
                
        if dupe_found == False:        
                import_lists.lists.append(new_list)

                write_data = open('import_lists.py', 'w')
                write_data.write("lists=" +str(import_lists.lists))
                write_data.close()
                DisplayAndSay("List titled, '" + title + "' successfully created.")
        else:
                DisplayAndSay("You already have a list titled '" + title +"'.")    

def Command7(UserVoiceInput):
        importlib.reload(import_lists)
        list_found = 0
        string_add = ''  #this is the element to be added to list

        title_found = False
        for i in VoiceArray:#iterates through voice string
            if title_found == True:#first so that when title is found, title is not added
                string_add = str(string_add + " " + i)
            for x in range(0, len(import_lists.lists)):#iterates throught lists
                if title_found == False:#ensures always matches the leftmost match
                    if i == import_lists.lists[x][0]:#attempts to match voice word with list title
                        title_found = True#ends matching attempts
                        list_found=x#index of list

                        
        if list_found == 0:
                DisplayAndSay("Could not find specified list.")
        else:
                DisplayAndSay("Adding: '" + string_add + "' to list '" +  import_lists.lists[list_found][0] +"'.")
                    
                import_lists.lists[list_found].append(string_add)

                write_data = open('import_lists.py', 'w')
                write_data.write("lists=" +str(import_lists.lists))
                write_data.close()
        


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

        DisplayAndSay("Alarm cancelled.")
        print([currentHour, currentMinute, currentFormat])
        print (import_alarms.alarms_list)                         
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()
def Command9(UserVoiceInput):
        player.pause()

def Search (UserVoiceInput):
        DisplayAndSay("I ran a search for " + UserVoiceInput +":")
        search=pypygo.query(UserVoiceInput)
        DisplayAndSay(search.abstract)


DisplayAndSay('Welcome to the TOMMY voice assistant. Press enter to get started.')
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
        CommandNineCount = 0
        

        next = input('hit enter for input')
        with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

        UserVoiceInput = r.recognize_wit(audio, key=WIT_AI_KEY)
        print(UserVoiceInput)
        #UserVoiceInput = input() #placeholder voice-interpreted text
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
            for x in range (0, len(CommandNineWords)):
                if VoiceArray[i] == CommandNineWords[x]:
                    CommandNineCount+=1

        ##--Command with most matches is called--##
        Counts = [CommandNineCount,CommandEightCount,CommandSevenCount,CommandSixCount,CommandFiveCount,CommandFourCount,CommandThreeCount,CommandTwoCount,CommandOneCount]

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
        elif CommandNineCount== Maximum:
            Command9(UserVoiceInput)
        else:
                Search(UserVoiceInput)
        
        

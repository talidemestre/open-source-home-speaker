# My code for switching between menus was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
import tkinter as tk

#modules for lists and alarms
import importlib
import os


LARGE_FONT= ("Verdana", 12)

#importing search
import wikipedia
import wolframalpha
client = wolframalpha.Client('8VTX85-9AA7GU7T3T')

#modules for alarms and lists
import time
import importlib

#importing external files
import import_calendar
import import_alarms
import import_perma_alarms
import import_lists

#modules for music search
import pafy
import vlc
import urllib.request
import urllib.parse
import re


#modules for speech recognition
import speech_recognition as sr
r = sr.Recognizer()
WIT_AI_KEY = "JL4IADZ4ODXSZ6RARKDP3IMMO66OSPS6"


#modules for text to speech
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
CommandTenWords = ["who", "when", "where", "why"]

#initialize player here, so music doesnt stack
Instance = vlc.Instance()
global player
player = Instance.media_player_new()
player.play()


##--Core Functions--##
def DisplayAndSay(text):
        print(text)
        out_text.configure(text=text)
        engine.say(text)        #vocalizes and displays the text
        engine.runAndWait()
        
##--Command Functions--##
def Command1(UserVoiceInput):
        global player
        player.stop() #stops any currently palying tracks before starting a new one
        search_term= ''
        found_song = False
        VoiceArray = UserVoiceInput.split(" ")
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
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        DisplayAndSay("Playing " + video.title + ".")
        player.play()

def Command2(UserVoiceInput):
        importlib.reload(import_alarms)
        importlib.reload(import_perma_alarms)
        VoiceArray = UserVoiceInput.split(" ")
        
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
        try:
                importlib.reload(import_calendar)

                testDate = UserVoiceInput.split(' ')
                finalMonth = int(time.strftime("%m"))
                finalDay=int(time.strftime("%d"))+1
                finalYear=int(time.strftime("%Y"))

                VoiceArray = UserVoiceInput.split(" ")
                
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
                                finalYear = y + import_calendar.creationYear
                        for z in range(0, len(daySuffix)):
                            if testDate[word+1] == daySuffix[z]:
                                finalDay= z + 20
                    if testDate[word] == 'thirty':
                        print("found")
                        for y in range(0, len(yearSuffix)):
                            if testDate[word+1] == yearSuffix[y]:
                                finalYear = y + import_calendar.creationYear
                        for z in range(0, len(daySuffix)):
                            if testDate[word+1] == daySuffix[z]:
                                print("made it")
                                finalDay= z + 30
                    if testDate[word] == 'two':
                        if testDate[word+1] == 'thousand':
                            for y in range(0, len(yearSuffix)):
                                if testDate[word+1] == yearSuffix[y] or testDate[word+2] == yearSuffix[y]:
                                    finalYear = y + import_calendar.creationYear

                #print(finalDay, finalMonth, finalYear)
                #writing results to the file that stores the calendar
                import_calendar.years[finalYear - int(time.strftime("%Y"))][finalMonth][finalDay] = UserVoiceInput
                write_data = open('import_calendar.py', 'w')
                write_data.write("creationYear=" + str(import_calendar.creationYear) + "\nyears =" + str(import_calendar.years))
                write_data.close()
                DisplayAndSay("Event set for " + str(finalDay+1) + " " + monthList[finalMonth] + " " + str(finalYear))
        except:
                 DisplayAndSay("Something went wrong in detecting the date. Please try again.")

##COMMAND THAT GATHERS EVENTS ON CALENDAR        
def Command4(UserVoiceInput):
        VoiceArray = UserVoiceInput.split(" ")
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

        VoiceArray = UserVoiceInput.split(" ")
        
        note_found=False

        #checking if note already exists
        for i in VoiceArray:
            if note_found == True:
                string_add = string_add + " " + i
            if i == 'note':
                note_found = True

        import_lists.lists[0].append(string_add)
        write_data = open('import_lists.py', 'w')
        write_data.write("lists=" +str(import_lists.lists))
        write_data.close()
        DisplayAndSay("Note: '" + string_add + "', added to notes.")
def Command6(UserVoiceInput):
        importlib.reload(import_lists)
        synonyms = ["list", "named", "called", "titled", "dubbed", "labelled", "termed", "christened", "denominated", "termed", "styled", "identified", "entititled", "termed"] #these are all synonyms for 'named' so that the program can determine what to name the list
        title_after=0 #position of last word before title, default
        VoiceArray = UserVoiceInput.split(" ")

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
        VoiceArray = UserVoiceInput.split(" ")
        
        title_found = False
        for i in VoiceArray:#iterates through voice string
            if title_found == True:#first so that when title is found, title is not added
                string_add = str(string_add + " " + i)
            for x in range(0, len(import_lists.lists)):#iterates throught lists
                if title_found == False:#ensures always matches the leftmost match
                    if i == import_lists.lists[x][0]:#attempts to match voice word with list title
                        title_found = True#ends matching attempts
                        list_found=x#index of list

        #checking if list already exists                     
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
        VoiceArray = UserVoiceInput.split(" ")
        
        print(time.strftime("%I"))
        print(time.strftime("%M"))
        print(time.strftime("%p"))

        #stops alarm from ringing        
        for i in (0, len(import_alarms.alarms_list)-1):
            if import_alarms.alarms_list[i][0] == currentHour:
                if import_alarms.alarms_list[i][1] == currentMinute:
                    if import_alarms.alarms_list[i][2] == currentFormat:
                         import_alarms.alarms_list.remove([currentHour, currentMinute, currentFormat])

        DisplayAndSay("Alarm cancelled.")
        print([currentHour, currentMinute, currentFormat])
        print (import_alarms.alarms_list)
        
        #deletes alarm from external file
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()
        
def Command9(UserVoiceInput):
        #pauses music
        player.pause()

def WikiSearch (UserVoiceInput):
        try:
                DisplayAndSay(wikipedia.summary(UserVoiceInput, sentences=1))
        except:
                try:
                        print(wikipedia.search(UserVoiceInput,results=2))
                        DisplayAndSay(wikipedia.summary(wikipedia.search(UserVoiceInput,results=2)[0], sentences =1))
                        #DisplayAndSay(wikipedia.page(title =wikipedia.search(UserVoiceInput,results=2)[0]).summary(sentences=2))
                except:
                        DisplayAndSay("Um. Something went wrong.")

def Search (UserVoiceInput):
        temp_process_math = UserVoiceInput.split()
        re_string = ''
        for i in temp_process_math:
                add=i
                print(i)
                if i == 'square':
                        add='squared'     #Wit AI often hears 'squared' as 'square; which causes it be a little shit. Hopefully this fixes that.
                re_string = re_string + add
                re_string = re_string + ' '
                print(re_string)
        res = client.query(re_string)
        print(res['@success'])
        print(res)
        if res['@success'] == 'false':
             WikiSearch(UserVoiceInput)
        else:
            try:
                DisplayAndSay(next(res.results).text)
            except:
                WikiSearch(UserVoiceInput)
        
####MAIN LOOP###
def MainLine():
    #DisplayAndSay('Welcome to the TOMMY voice assistant. Press enter to get started.')

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
    CommandTenCount = 0
    

    #next = input('hit enter for input')
    with sr.Microphone() as source:
            print ("Listening:")
            audio = r.listen(source,timeout=2,phrase_time_limit=6)
    print("processing...")
    UserVoiceInput = r.recognize_wit(audio, key=WIT_AI_KEY)
    #UserVoiceInput = input("debug manual input: ")
    print(UserVoiceInput)
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
        for x in range (0, len(CommandTenWords)):
            if VoiceArray[i] == CommandTenWords[x]:
                CommandTenCount+=1                

    ##--Command with most matches is called--##
    Counts = [CommandTenCount, CommandNineCount,CommandEightCount,CommandSevenCount,CommandSixCount,CommandFiveCount,CommandFourCount,CommandThreeCount,CommandTwoCount,CommandOneCount]

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
    elif CommandTenCount== Maximum:
        WikiSearch(UserVoiceInput)
    else:
            Search(UserVoiceInput)
        
        



###############################################################################

#The following functions write to external files.
def WriteAlarm(alarms_list):
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(alarms_list))
        write_data.close()
        
def WritePermaAlarm(alarms_list):
        write_data = open('import_perma_alarms.py', 'w')
        write_data.write("alarms_list=" + str(alarms_list))
        write_data.close()

def WriteList(lists):
        write_data = open('import_lists.py', 'w')
        write_data.write("lists=" +str(import_lists.lists))
        write_data.close()        

###This is the beginning of tkinter(gui) code

#This is the code used as the root for all of the other pages.
class Pages(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        #all other pages must be in this loop
        for F in (Main, Settings, Demo, Demo2, Demo3, ShellTom, ReadLists):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#This is the page you see upon first starting the program.        
class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="T.O.M.M.Y Voice Assistant", font=LARGE_FONT)
        label.pack(pady=8,padx=10)
        
        config_button = tk.Button(self,width=10,  text="Config",fg="red",
                              command=lambda: controller.show_frame(Settings))
        config_button.pack(pady=12)

        run_button = tk.Button(self,width=10,  text="Run Assistant", fg="brown", 
                                command=lambda: controller.show_frame(ShellTom))
        run_button.pack(pady=12)

        demo_button = tk.Button(self,width=10,  text="Demo", fg="blue",
                                command=lambda: controller.show_frame(Demo))
        demo_button.pack(pady=12)

        back_button = tk.Button(self,width=10,  text="Quit", fg="black", bg="green",
                                command=lambda: exit())
        back_button.pack( side = tk.BOTTOM )

#This is the page labelled 'config'.
class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=2,padx=10)
        
        #list label
        redbutton = tk.Label(self, width=10, text="Lists",  fg="red")
        redbutton.pack()

        ##LIST BUTTONS
        list_frame = tk.Frame(self)
        list_frame.pack()
        for List in import_lists.lists:
            if List[0]!='notes':
                button =tk.Button(list_frame, width =10, text = List[0])
                button['command'] = lambda x=List, y=button: (import_lists.lists.remove(x), y.pack_forget(), self.update(), WriteList(import_lists.lists))
                button.pack(side = tk.LEFT)
           




        #alarms label
        greenbutton = tk.Label(self,width=10,  text="Alarms", fg="brown")
        greenbutton.pack()

        ##ALARM BUTTONS
        button_array=['','','','','','','','','','','','','','','','','','',]
        alarm_frame = tk.Frame(self)
        alarm_frame.pack()
        for Alarm in import_alarms.alarms_list:
            alarm_button =tk.Button(alarm_frame, width =10, text = Alarm)
            alarm_button['command'] = lambda x=Alarm, y=alarm_button:( import_alarms.alarms_list.remove(x),
                                                y.pack_forget(),
                                                self.update(),
                                                WriteAlarm(import_alarms.alarms_list)
                                                )
            alarm_button.pack(side = tk.LEFT)



        #perma label
        perma_label = tk.Label(self, width=15, text="Permanent Alarms",  fg="Blue")
        perma_label.pack()
        
        ##PERMA ALARM BUTTONS        
        perma_alarm_frame = tk.Frame(self)
        perma_alarm_frame.pack()        
        for Alarm in import_perma_alarms.alarms_list:
            perma_button =tk.Button(perma_alarm_frame, width=10, text = Alarm)
            perma_button['command'] = lambda x=Alarm, y=perma_button:( import_perma_alarms.alarms_list.remove(x),
                                                y.pack_forget(),
                                                self.update(),
                                                WritePermaAlarm(import_perma_alarms.alarms_list)
                                                )
            perma_button.pack(side = tk.LEFT)


        volume_label =tk.Label(self, text="Volume")
        volume_label.pack()
        
        volume_bar = tk.Scale(self,width=10, orient=tk.HORIZONTAL, showvalue=0 )
        volume_bar.set(100)
        #this allows the volume of the raspberry pi device to be controlled
        volume_bar['command'] = lambda y=volume_bar: os.system("amixer sset 'PCM' " + str(volume_bar.get()) + "%")   #doesn't work on windows                                           
        volume_bar.pack( )

        
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                                command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

#the next 3 classes are the 'frames' of a slideshow that teach the user how to use the software
class Demo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Step 1", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        step_1 = tk.Label(self, width=80, text="Many commands are in the TOMMY Voice Assistant.",  fg="Blue")
        step_1.pack()

        step_2 = tk.Label(self, width=80, text="To begin tap the 'Run Assistant' button.",  fg="Blue")
        step_2.pack()

        button_left = tk.Button(self, text="Back",state =tk.DISABLED)
        button_left.pack(side = tk.LEFT)

        button2 = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(Demo2))
        button2.pack(side = tk.RIGHT)

        ##importing images
        self.step1 = tk.PhotoImage(file="step1.gif")

        image = tk.Label(self, image = self.step1)
        image.image = self.step1
        image.pack()    

        
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                         command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

class Demo2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Step 2", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        step_1 = tk.Label(self, width=80, text="Next tap the 'Ask Question' button.",  fg="Blue")
        step_1.pack()

        step_2 = tk.Label(self, width=80, text="Speak your request into the microphone.",  fg="Blue")
        step_2.pack()

        button_left = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(Demo))
        button_left.pack(side = tk.LEFT)

              
        button2 = tk.Button(self, text="Next",
                            command=lambda: controller.show_frame(Demo3))
        button2.pack(side=tk.RIGHT)

        self.step2 = tk.PhotoImage(file="step2.gif")

        image = tk.Label(self, image = self.step2)
        image.image = self.step2
        image.pack()    

        
        
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                         command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

class Demo3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Step 3", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        step_1 = tk.Label(self, width=80, text="Wait for your result to process...",  fg="Blue")
        step_1.pack()

        step_2 = tk.Label(self, width=80, text="This is how to use the simple interface.",  fg="Blue")
        step_2.pack()


        button_left = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(Demo2))
        button_left.pack(side = tk.LEFT)

        button2 = tk.Button(self, text="Next", state = tk.DISABLED)
        button2.pack(side=tk.RIGHT)


        self.step3 = tk.PhotoImage(file="step3.gif")

        image = tk.Label(self, image = self.step3)
        image.image = self.step3
        image.pack()    

        
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                         command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

#this is the menu from which the user asks questions
class ShellTom(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Program", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        ask_quest = tk.Button(self, width = 20, height=5, text="Ask Question",
                            command=lambda: MainLine())
        ask_quest.pack(pady=5)


        global out_text #lets TOMMY display what he is saying
        out_text = tk.Label(self, text="")
        out_text.pack()

        view_lists = tk.Button(self, width = 20, text="View Lists",
                            command=lambda: controller.show_frame(ReadLists))
        view_lists.pack(pady=5)        

        back_button = tk.Button(self, width=10,  text="Back", fg="black", bg="green",
                         command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )
#the menu the viewer reads lists from
class ReadLists(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lists", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        list_labels=[]
        list_text=[]

        #generates label objects for each list and then packs them into the tkinter frame
        for array in range(0, len(import_lists.lists)):
                
                list_text.append('')
                
                for item in range(0, len(import_lists.lists[array])):
                               if item == 0:
                                       list_text[array]= list_text[array] + str(import_lists.lists[array][item]).capitalize() + ':'
                               else:
                                       list_text[array] = list_text[array]  + ', ' + import_lists.lists[array][item]
                                       
        for i in range(0, len(list_text)):
                list_labels.append(tk.Label(self, text=list_text[i], fg='blue'))
                list_labels[i].pack()
                
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                         command=lambda: controller.show_frame(ShellTom))
        back_button.pack( side = tk.BOTTOM )

#initiates tkinter        
app = Pages()
app.geometry("320x240")
app.attributes('-fullscreen', True)
app.mainloop()

#UserVoiceInput = "Hey google, set an alarm for four thirty"
UserVoiceInput = "write a note for me" #placeholder voice-interpreted text

VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable

#print (VoiceArray) ##DEBUG LINE

##--Trigger Words For Each Command--##
CommandOneWords = ["play", "music", "song"]
CommandTwoWords = ["set", "alarm"]
CommandThreeWords = ["calendar", "event","date","schedule"]
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
        print ("Attempting to set calendar...")
def Command4(UserVoiceInput):
        print ("Attempting to gather schedule...")
def Command5(UserVoiceInput):
        print ("Attempting to write note...")
def Command6(UserVoiceInput):
        print ("Attempting to add to list...")
def Command7(UserVoiceInput):
        print ("Attempting to create list...")

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

if CommandOneCount== Maximum:
    Command1(UserVoiceInput)
if CommandTwoCount== Maximum:
    Command2(UserVoiceInput)
if CommandThreeCount== Maximum:
    Command3(UserVoiceInput)
if CommandFourCount== Maximum:
    Command4(UserVoiceInput)
if CommandFiveCount== Maximum:
    Command5(UserVoiceInput)
if CommandSixCount== Maximum:
    Command6(UserVoiceInput)
if CommandSevenCount== Maximum:
    Command7(UserVoiceInput)

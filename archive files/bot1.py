UserVoiceInput = "Hey google, set alarm"

VoiceArray = UserVoiceInput.split(" ")
print (VoiceArray)


CommandOneWords = ["play", "music"]
CommandTwoWords = ["set", "alarm"]

CommandOneCount = 0
CommandTwoCount = 0

def Command1(UserVoiceInput):
        print ("Attempting to play music...")

def Command2(UserVoiceInput):
        print ("Attempting to set Alarm...")
        
for i in range (0, len(VoiceArray)):
    for x in range (0, len(CommandOneWords)):
        if VoiceArray[i] == CommandOneWords[x]:
            CommandOneCount+=1
    for x in range (0, len(CommandTwoWords)):
        if VoiceArray[i] == CommandTwoWords[x]:
            CommandTwoCount+=1



if CommandOneCount>CommandTwoCount:
    Command1(UserVoiceInput)

if CommandTwoCount>CommandOneCount:
    Command2(UserVoiceInput)

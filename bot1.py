UserVoiceInput = "execute command two"

VoiceArray = UserVoiceInput.split(" ")
print (VoiceArray)


CommandOneWords = ["command", "one"]
CommandTwoWords = ["command", "two"]

CommandOneCount = 0
CommandTwoCount = 0

def Command1(UserVoiceInput):
        print ("This is the first command")

def Command2(UserVoiceInput):
        print ("This is the second command")
        
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

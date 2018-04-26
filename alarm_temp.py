import time

UserVoiceInput = "set an alarm for five thirty seven"#placeholder voice-interpreted text
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ")

hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

minuteMono = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
minutePrefix =['twenty','thirty','fourty','fifty','sixty']
minuteSuffix =['one', 'two', 'three', 'four', 'five', "six", "seven", "eight", "nine"]

finalHour=0
finalMinute=0

AMorPM = "PM" ###DEFAULT PLEASE CHANGE###

hour_detected = False

for word in range(0, len(VoiceArray)):
    print (VoiceArray[word])
    if VoiceArray[word] == 'AM':#
        AMorPM ="AM"#
    if VoiceArray[word] == 'PM':#The voice detection will likely not read these as AM or PM and as such they should be updated.
        AMorPM ="PM" #               
    if hour_detected == False:
        for num in range (0, len(hourList)):
            if VoiceArray[word] == hourList[num]:
                hour_detected = True
                finalHour = word+1              
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

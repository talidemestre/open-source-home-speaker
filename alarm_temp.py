import time

UserVoiceInput = "set an alarm for five thirty seven"#placeholder voice-interpreted text
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ")

hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

minuteMono = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
minutePrefix =['twenty','thirty','fourty','fifty','sixty']
minuteSuffix =['one', 'two', 'three', 'four', 'five', "six", "seven", "eight", "nine"]





hour_word = ""
minute_mono_word = ""
minute_prefix_word = ""
minute_suffix_word = ""


AMorPM = "PM" ###DEFAULT PLEASE CHANGE###



hour_detected = False
for word in range(0, len(VoiceArray)):
    print (VoiceArray[word])
    if hour_detected == False:
        for num in range (0, len(hourList)):
            if VoiceArray[word] == hourList[num]:
                hour_detected = True
                hourFoundAt = word
                hour_word = VoiceArray[word]               
    else:
        for num in range (0, len(minuteMono)):
            if VoiceArray[word] == minuteMono[num]:
                minute_mono_word = VoiceArray[word]
        for num in range (0, len(minutePrefix)):
            if VoiceArray[word] == minutePrefix[num]:
                minute_prefix_word = VoiceArray[word]
        for num in range (0, len(minuteSuffix)):
            if VoiceArray[word] == minuteSuffix[num]:
                minute_suffix_word = VoiceArray[word]
                
##Converting Words into Numbers##
finalHour=0
finalMinute=0

for i in range (0, len(hourList)):
    if hour_word == hourList[i]:
        finalHour = i+1

if minute_mono_word == '':
    if minute_prefix_word != '':
        for i in range (0, len(minutePrefix)):
            if minute_prefix_word == minutePrefix[i]:
                finalMinute+= 10*((i+2))
                                  
    if minute_suffix_word != '':                                  
        for i in range (0, len(minuteSuffix)):
            if minute_suffix_word == minuteSuffix[i]:
                finalMinute += i+1
else:
    for i in range (0, len(minuteMono)):
        if minute_mono_word == minuteMono[i]:
            finalMinute = i + 10
    
    

import time
import import_alarms

UserVoiceInput = "set an alarm for one two ten"#placeholder voice-interpreted text
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ")

hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

minuteMono = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
minutePrefix =['twenty','thirty','fourty','fifty']
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

                
##CHECK ALARM##
for i in (0, len(import_alarms.alarms_list)-1):
    for x in (0, len(import_alarms.alarms_list[i])):
        if import_alarms.alarms_list[i][2] == 'AM':
            if int(time.strftime("%H"))==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]:
                print("alarm is sounding")
        else:
            if int(time.strftime("%H")) - 12 ==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]:
                print("alarm is sounding")
        

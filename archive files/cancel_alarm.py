import time
import import_alarms

print(time.strftime("%H"))
print(time.strftime("%M"))
print(time.strftime("%p"))

currentHour=int(time.strftime("%H"))
currentMinute=int(time.strftime("%M"))
currentFormat=time.strftime("%p")

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

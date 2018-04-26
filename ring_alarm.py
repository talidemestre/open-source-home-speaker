import time
##CHECK ALARM##
import importlib
import import_alarms

while True:
    print(import_alarms.alarms_list)
    importlib.reload(import_alarms)
    if len(import_alarms.alarms_list) >0:
            for i in (0, len(import_alarms.alarms_list)-1):
                for x in (0, len(import_alarms.alarms_list[i])):
                    if import_alarms.alarms_list[i][2] == 'AM':
                        if int(time.strftime("%H"))==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]:
                            print("alarm is sounding")
                    else:
                        if int(time.strftime("%H")) - 12 ==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]:
                            print("alarm is sounding")
            time.sleep(1)


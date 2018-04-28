import time
##CHECK ALARM##
import importlib
import import_alarms
import import_perma_alarms
startup=0

while True:
    print(import_alarms.alarms_list)
    importlib.reload(import_alarms)
    importlib.reload(import_perma_alarms)
    if len(import_alarms.alarms_list) >0:
            for i in (0, len(import_alarms.alarms_list)-1):
                for x in (0, len(import_alarms.alarms_list[i])):
                    if import_alarms.alarms_list[i][2] == 'AM': 
                        if int(time.strftime("%H"))==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]: #Checking if Alarms on the AM are in the current hour and minute
                            print("alarm is sounding")
                    else:
                        if int(time.strftime("%H")) - 12 ==import_alarms.alarms_list[i][0] and int(time.strftime("%M"))==import_alarms.alarms_list[i][1]:#Checking if Alarms on the PM are in the current hour and minute
                            print("alarm is sounding")
            time.sleep(1)
    if int(time.strftime("%H"))== 2 and int(time.strftime("%M"))==33 or startup==0:
        startup=1
        for i in import_perma_alarms.alarms_list:
            match=False
            for x in import_alarms.alarms_list:
                if x == i:
                    match =True
            if match == False:
                import_alarms.alarms_list.append(i)


        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(import_alarms.alarms_list))
        write_data.close()



import import_alarms
import import_perma_alarms
print(import_alarms.alarms_list)
print(import_perma_alarms.alarms_list)

for i in import_perma_alarms.alarms_list:
    match=False
    for x in import_alarms.alarms_list:
        if x == i:
            match =True
    if match == False:
        import_alarms.alarms_list.append(i)

print("\n")
print(import_alarms.alarms_list)

write_data = open('import_alarms.py', 'w')
write_data.write("alarms_list=" + str(import_alarms.alarms_list))
write_data.close()


import import_lists
import importlib
importlib.reload(import_lists)

UserVoiceInput = "add to berrys grow pomegranites"
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable

print (import_lists.lists)




list_found = 0
string_add = ''  #this is the element to be added to list

title_found = False
for i in VoiceArray:#iterates through voice string
    if title_found == True:#first so that when title is found, title is not added
        string_add = str(string_add + " " + i)
    for x in range(0, len(import_lists.lists)-1):#iterates throught lists
        if title_found == False:#ensures always matches the leftmost match
            if i == import_lists.lists[x][0]:#attempts to match voice word with list title
                title_found = True#ends matching attempts
                list_found=x#index of list

            
import_lists.lists[list_found].append(string_add)

write_data = open('import_lists.py', 'w')
write_data.write("lists=" +str(import_lists.lists))
write_data.close()

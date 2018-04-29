import import_lists
import importlib
importlib.reload(import_lists)


UserVoiceInput = "create a list called berrys"
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable


synonyms = ["list", "named", "called", "titled", "dubbed", "labelled", "termed", "christened", "denominated", "termed", "styled", "identified", "entititled", "termed"] #these are all synonyms for 'named' so that the program can determine what to name the list
title_after=0 #position of last word before title, default


title = 'list' #default title


#searching for synonym of 'named'
for i in range(0, len(VoiceArray)):
    for x in synonyms:
        if VoiceArray[i] == x:
            title_after = i



#allocating title
title = VoiceArray[title_after + 1]

new_list = [title]

dupe_found = False#tests if title is duplicate of existing title
for i in import_lists.lists:
    if i[0] == title:
        dupe_found = True
        
if dupe_found == False:        
    import_lists.lists.append(new_list)

    write_data = open('import_lists.py', 'w')
    write_data.write("lists=" +str(import_lists.lists))
    write_data.close()
else:
    print("You already have a list titled with that.")    

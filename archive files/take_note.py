import import_lists
import importlib
importlib.reload(import_lists)


UserVoiceInput = "take a note Harold Holt note was born note August Fifth."
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable

string_add=''

note_found=False

for i in VoiceArray:
    if note_found == True:
        string_add = string_add + " " + i
    if i == 'note':
        note_found = True

import_lists.lists[0].append(string_add)

write_data = open('import_lists.py', 'w')
write_data.write("lists=" +str(import_lists.lists))
write_data.close()

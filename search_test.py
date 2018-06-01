import pypygo
import wikipedia

UserVoiceInput = input("aaaaaaaaa")
print("I ran a search for " + UserVoiceInput +":")

try:
    search=pypygo.query(UserVoiceInput)
except:
    print("error")



try: #getting results of user question
    print (wikipedia.summary(UserVoiceInput, sentences=2))
except wikipedia.exceptions.DisambiguationError: #handling disambiguation pages
    print (wikipedia.search(UserVoiceInput,results=2))
    print (wikipedia.summary(wikipedia.search(UserVoiceInput,results=2)[1], sentences=2))
    

#print(search.abstract)

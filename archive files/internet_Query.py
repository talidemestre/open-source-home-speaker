import pypygo

UserVoiceInput = "who is president obama"
search=pypygo.query(UserVoiceInput)
print(search.abstract)

UserVoiceInput = "set an alarm for four fifty seven"#placeholder voice-interpreted text
UserVoiceInput = UserVoiceInput.lower()
VoiceArray = UserVoiceInput.split(" ")
hourList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']



AMorPM = "PM" ###DEFAULT PLEASE CHANGE###
for word in range(0, len(VoiceArray)):

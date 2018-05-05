import pafy
import vlc
import urllib.request
import urllib.parse
import re


UserVoiceInput = 'play the seinfeld theme'


VoiceArray = UserVoiceInput.split(" ") #turns the voice input into an iterable
print(VoiceArray)

search_term= ''
found_song = False

#extracts everything after either the first 'play' or first 'song'
for i in VoiceArray:
    if found_song == True:
        search_term = search_term +' ' + i
    else:
        if i == 'song' or i =='play':
            found_song = True


#searches for user song, credit of Grant Curell https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
query_string = urllib.parse.urlencode({"search_query" : search_term + 'song'}) #'song' added to end to lower chance of non-song results
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]

print(url)

#extracts audio from selected song's youtbe video
video = pafy.new(url)
best = video.getbestaudio()
playurl = best.url


#plays selected song in vlc
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()

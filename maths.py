import wolframalpha
client = wolframalpha.Client('8VTX85-9AA7GU7T3T')


UserVoiceInput = input('asdadsadad')

res = client.query(UserVoiceInput)

if res['@success'] == 'false':
     print('CALL WIKI SEARCH')
else:
    try:
        print(next(res.results).text)
    except:
        print('CALL WIKI SEARCH')

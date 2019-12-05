import json
import requests
vote = 'heysan'
id = '826507'
data = {"question_type":"wordcloud","vote":vote}
#{"question_type":"wordcloud","vote":"asdfghjkl"}
data_json = json.dumps(data)

#while(1):

s = requests.get('https://www.menti.com/core/objects/vote_ids/'+id)
parsedId = s.json()['id']

s = requests.post('https://www.govote.at/core/identifier')
#print(s)
identifier = s.json()['identifier']
print(identifier)

headers = {'x-identifier': identifier}

r = requests.post('https://www.govote.at/core/votes/'+parsedId, json = data, headers = headers)
print(r.text)

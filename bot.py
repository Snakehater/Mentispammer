import json
import requests
vote = 
question = ''
data = {"question": question, "question_type": "choices", "vote": vote}
data_json = json.dumps(data)

while(1):
  s = requests.post('https://www.govote.at/api/identifier')
  identifier = s.json()['identifier']
  
  headers = {'x-identifier': identifier}
  
  r = requests.post('https://www.govote.at/api/vote', json = data, headers = headers)  
  print r.text


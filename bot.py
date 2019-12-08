import json
import requests
vote = 'nej'
vote = input('Text: ')
id = '200724'
id = input('Id: ')
data = {"question_type":"wordcloud","vote":vote}
#{"question_type":"wordcloud","vote":"asdfghjkl"}
data_json = json.dumps(data)

#while(1):

s = requests.get('https://www.menti.com/core/objects/vote_ids/'+id)
parsedId = s.json()['id']

print(parsedId)

s = requests.get('https://www.menti.com/core/objects/vote_keys/'+parsedId)

str = s.text
print(str)
jsondata = json.loads(str)
question = jsondata['questions'][0]
parsedKey = question['public_key']
print(parsedKey)

# headers = {'x-identifier': identifier}
# headers = {
#   ":authority": "www.menti.com",
#   ":method": "POST",
#   ":path": "/core/votes/9af3bee66484",
#   ":scheme": "https",
#   "accept": "application/json",
#   "accept-encoding": "gzip, deflate, br",
#   "accept-language": "en-US,en;q=0.9",
#   "content-lengt": "42",
#   "content-type": "application/json; charset=UTF-8",
#   "cookie": "_ga=GA1.2.1555705289.1573573435; _fbp=fb.1.1573573435740.1944003412; identifier1=7638a15c4ae5370ebf092821bf45f495770f8eec1c64a782337013cb5f77a42c; _gid=GA1.2.1316845992.1575545568; _gat=1; _gat_UA-23693781-9=1; _gat_UA-23693781-3=1",
#   "origin": "https://www.menti.com",
#   "referer": "https://www.menti.com/"+parsedId,
#   "sec-fetch-mode": "cors",
#   "sec-fetch-site": "same-origin",
#   "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48",
#   "x-identifier": identifier
# }
# ':authority': 'www.menti.com',':method': 'POST',':path': '/core/votes/9af3bee66484',':scheme': 'https',



for x in range(6):

    s = requests.post('https://www.govote.at/core/identifier')
    #print(s)
    identifier = s.json()['identifier']
    print(identifier)
    headers = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-lengt': '42','content-type': 'application/json; charset=UTF-8','cookie': '_ga=GA1.2.1555705289.1573573495; _fbp=fb.1.1573573435740.1944003412; identifier1='+identifier+'; _gid=GA1.2.1316845992.1575545568; _gat=1; _gat_UA-23693781-9=1; _gat_UA-23693781-3=1','origin': 'https://www.menti.com','referer': 'https://www.menti.com/'+parsedId,'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48','x-identifier': identifier}

    # print(headers)

    r = requests.post('https://www.govote.at/core/votes/'+parsedKey, json = data, headers = headers)
    print(r.text)

import json
import grequests
import requests
import _thread
import time
id = '200724'
id = input('Id: ')
voteText = ['nej']
voteIdx = 0
voteText[0] = input('Text: ')
while True:
    inputText = input('Add text, press enter without text to proceed: ')
    if inputText == "":
        break
    else:
        voteText.append(inputText)
threads = eval(input("Threads: "))
numberOfRequests = eval(input("Requests: "))
numberOfRequests *= len(voteText)
requestCount = 0
requestDoneCount = 0
scriptAlive = True
# data = {"question_type":"wordcloud","vote":voteText}
#{"question_type":"wordcloud","vote":"asdfghjkl"}
# data_json = json.dumps(data)

#while(1):

s = requests.get('https://www.menti.com/core/objects/vote_ids/'+id)
parsedId = s.json()['id']

print(parsedId)

s = requests.get('https://www.menti.com/core/objects/vote_keys/'+parsedId)

string = s.text
print(string)
jsondata = json.loads(string)
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


    # for x in range(6):

def vote(voteIn):
    newdata = {"question_type":"wordcloud","vote":voteIn}
    # s = grequests.post('https://www.govote.at/core/identifier')
    #print(s)
    # identifier = s.json()['identifier']
    content = ""
    urls = ['https://www.govote.at/core/identifier']
    rs = (grequests.post(u) for u in urls)
    requests = grequests.map(rs)
    for response in requests:
        content = response.content

    identifier = json.loads(content)['identifier']

    print(identifier)
    headers = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-lengt': '42','content-type': 'application/json; charset=UTF-8','cookie': '_ga=GA1.2.1555705289.1573573495; _fbp=fb.1.1573573435740.1944003412; identifier1='+identifier+'; _gid=GA1.2.1316845992.1575545568; _gat=1; _gat_UA-23693781-9=1; _gat_UA-23693781-3=1','origin': 'https://www.menti.com','referer': 'https://www.menti.com/'+parsedId,'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48','x-identifier': identifier}

    # print(headers)
    content = ""
    urls2 = ['https://www.govote.at/core/votes/'+parsedKey]
    rs = (grequests.post(u, json = newdata, headers = headers) for u in urls2)
    requests = grequests.map(rs)
    for response in requests:
        content = response
    print(content)


# vote(voteText)

def checkScriptAlive(threadName):
    global scriptAlive
    while True:
        if requestDoneCount == numberOfRequests:
            scriptAlive = False;
            break

def threadFun(threadName):
    # time.sleep(delay)
    global requestCount
    global voteIdx
    global voteText
    global requestDoneCount
    while requestCount < numberOfRequests:
        requestCount += 1
        if voteIdx == len(voteText):
            voteIdx = 0

        text = voteText[voteIdx]
        voteIdx += 1

        print(str(threadName) + " Requests " + str(requestCount) + " with " + str(text))
        vote(text)
        requestDoneCount += 1

def startThreads():
    _thread.start_new_thread( checkScriptAlive, ("Thread-checkScriptAlive", ) )
    for idx in range(threads):
        _thread.start_new_thread( threadFun, ("Thread-" + str(idx), ) )
        time.sleep(0.2)
# def startListThreads(arg):
#     for idx in range(threads):
#         _thread.start_new_thread( threadFun, ("Thread-" + str(idx), ) )
#         time.sleep(0.2)

startThreads()
while scriptAlive:
    pass

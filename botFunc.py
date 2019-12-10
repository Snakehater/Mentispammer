import json
import grequests
import requests
import _thread
import time

class Bot:
    threads = 0
    numberOfRequests = 0
    numberOfRequests *= 1
    requestCount = 0
    requestDoneCount = 0
    voteIdx = 0
    voteText = []
    parsedId = ""
    def __init__(self, parsedId, voteText, threads, numberOfRequests, perWord):
        self.parsedId = parsedId
        self.voteText = voteText
        self.threads = threads
        self.numberOfRequests = numberOfRequests
        if perWord:
            self.numberOfRequests *= len(self.voteText)

        startThreads(parsedId)


    # def defNew(voteTextIn, threadsIn, numberOfRequestsIn, numberOfRequestsMultiIn, requestCountIn, requestDoneCountIn):
    #     reset()
    #     self.threads = threadsIn
    #     self.numberOfRequests = numberOfRequestsIn
    #     self.numberOfRequests *= numberOfRequestsMultiIn
    #     self.requestCount = requestCountIn
    #     self.requestDoneCount = requestDoneCountIn
    #     self.voteText = voteTextIn

    # def reset():
    #     self.threads = 0
    #     self.numberOfRequests = 0
    #     self.requestCount = 0
    #     self.requestDoneCount = 0
    #     self.voteIdx = 0

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

    def threadFun(threadName):
        # time.sleep(delay)
        # global requestCount
        # global voteIdx
        # global voteText
        # global requestDoneCount
        while self.requestCount < self.numberOfRequests:
            self.requestCount += 1
            if self.voteIdx == len(self.voteText):
                self.voteIdx = 0

            text = self.voteText[voteIdx]
            self.voteIdx += 1

            print(str(threadName) + " Requests " + str(self.requestCount) + " with " + str(text))
            self.vote(text)
            self.requestDoneCount += 1

    def startThreads(parsedId):
        s = requests.get('https://www.menti.com/core/objects/vote_keys/'+parsedId)

        string = s.text
        jsondata = json.loads(string)
        question = jsondata['questions'][0]
        parsedKey = question['public_key']
        print("Key: " + str(parsedKey))
        for idx in range(self.threads):
            _thread.start_new_thread( self.threadFun, ("Thread-" + str(idx), ) )
            time.sleep(0.2)

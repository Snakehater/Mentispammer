# import json
# import grequests
# import requests
# import _thread
# import time

class Bot:
    threads = 0
    numberOfRequests = 0
    numberOfRequests *= 1
    requestCount = 0
    requestDoneCount = 0
    voteIdx = 0
    voteText = []
    parsedId = ""
    parsedKey = ""
    done = False

    json = __import__('json')
    grequests = __import__('grequests')
    requests = __import__('requests')
    _thread = __import__('_thread')
    time = __import__('time')
    mttkinter = __import__('mttkinter')
    tk = mttkinter.mtTkinter
    threading = __import__('threading')
    math = __import__('math')
    def updateProgress(self):
        self.percentage = round(100*(self.requestDoneCount/self.numberOfRequests), 1)
        print(self.percentage)

        oldLabel = self.logLabel.cget("text")
        if oldLabel != str(self.percentage) + '%':
            self.logLabel.configure(text=(str(self.percentage) + '%'))
            barStr ='__________'
            barStrList = list(barStr)
            for idx in range(self.math.floor(self.percentage/10)):
                barStrList[idx] = '#'
            barStr = ''.join(barStrList)
            self.logText.configure(text=barStr)

        if self.percentage == 100.0:
            self.stop()
            
    def printw(self, string):
        # self.addText(string)
        # self.root.after(5000, lambda: self.addText(string))
        pass
    def addText(self, string):
        old = self.logText.cget("text")
        new = old+"\n"+string
        self.logText.configure(text=new)
    def __init__(self, threadToCall, parsedId, voteText, threads, numberOfRequests, perWord):
        self.threadToCall = threadToCall
        self.done = False
        self.parsedId = parsedId
        self.voteText = voteText
        self.threads = threads
        self.numberOfRequests = numberOfRequests
        if perWord:
            self.numberOfRequests *= len(self.voteText)


        self.root = self.tk.Tk()

        self.root.bind("<Destroy>", self.destroy)

        self.logLabel = self.tk.LabelFrame(self.root, text="0%")

        self.logText=self.tk.Label(self.logLabel, text='__________', height=1, width=10, anchor='nw', justify='left')
        self.logLabel.pack(padx=10, pady=10, side='top')
        self.logText.pack()

        self.stopBtn = self.tk.Button(self.root, text='Stop', command=(lambda: self.stop()))
        self.stopBtn.pack(side='bottom')

        self.startThreads()

        self.tk.mainloop()

    def destroy(self, event):
        self.stop()

    def stop(self):
        self.done = True
        self.stopBtn.update()
        # self.time.sleep(2)
        self.root.destroy()
        self.callThread()
        # self.exit()
    def callThread(self):
        self.threadToCall.start()

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

    def vote(self, voteIn):
        newdata = {"question_type":"wordcloud","vote":voteIn}
        # s = grequests.post('https://www.govote.at/core/identifier')
        #print(s)
        # identifier = s.json()['identifier']
        content = ""
        urls = ['https://www.govote.at/core/identifier']
        rs = (self.grequests.post(u) for u in urls)
        requests = self.grequests.map(rs)
        for response in requests:
            content = response.content

        identifier = self.json.loads(content)['identifier']

        self.printw(identifier)
        headers = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-lengt': '42','content-type': 'application/json; charset=UTF-8','cookie': '_ga=GA1.2.1555705289.1573573495; _fbp=fb.1.1573573435740.1944003412; identifier1='+identifier+'; _gid=GA1.2.1316845992.1575545568; _gat=1; _gat_UA-23693781-9=1; _gat_UA-23693781-3=1','origin': 'https://www.menti.com','referer': 'https://www.menti.com/'+self.parsedId,'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48','x-identifier': identifier}

        # print(headers)
        content = ""
        urls2 = ['https://www.govote.at/core/votes/'+self.parsedKey]
        rs = (self.grequests.post(u, json = newdata, headers = headers) for u in urls2)
        requests = self.grequests.map(rs)
        for response in requests:
            content = response
        self.printw(content)


    # vote(voteText)

    def threadFun(self, threadName):
        # time.sleep(delay)
        # global requestCount
        # global voteIdx
        # global voteText
        # global requestDoneCount
        while self.requestCount < self.numberOfRequests and self.done is False:
            self.requestCount += 1
            if self.voteIdx == len(self.voteText):
                self.voteIdx = 0

            text = self.voteText[self.voteIdx]
            self.voteIdx += 1

            self.printw(str(threadName) + " Requests " + str(self.requestCount) + " with " + str(text))
            self.vote(text)
            self.requestDoneCount += 1
            self.updateProgress()

    def startThreads(self):
        s = self.requests.get('https://www.menti.com/core/objects/vote_keys/'+self.parsedId)

        string = s.text
        jsondata = self.json.loads(string)
        question = jsondata['questions'][0]
        parsedKey = question['public_key']
        self.parsedKey = parsedKey
        self.printw("Key: " + str(parsedKey))
        for idx in range(self.threads):
            # self._thread.start_new_thread( self.threadFun, ("Thread-" + str(idx), ) )
            t = self.threading.Thread(target=(lambda: self.threadFun("Thread-" + str(idx), )))
            t.start()
            self.time.sleep(0.2)

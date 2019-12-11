from botFunc import Bot
import tkinter as tk
import requests


root = tk.Tk()
parsedId = ""
perWord = tk.BooleanVar()

def validate(action, value_if_allowed):
    if value_if_allowed:
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return True
remIdx = lambda x, unwanted : ''.join([ c for i, c in enumerate(x) if i != unwanted])
def replaceDoubleNewLine(string):
    outString = string
    idx = 0
    charBefore = ''
    for char in string:
        if charBefore == '\n' and char == '\n':
            outString = remIdx(outString, idx)
        else:
            idx += 1
        charBefore = char
    return outString

def replaceExtraNewLine(string):
    outString = string
    idx = 0
    charBefore = ''
    for char in string:
        if idx == 0 and char == '\n':
            outString = remIdx(outString, idx)
        elif charBefore == '\n' and char == '\n':
            outString = remIdx(outString, idx)
        elif idx == len(outString)-1 and char == '\n':
            outString = remIdx(outString, idx)
        else:
            idx += 1
        charBefore = char
    return outString

def resizeTextField(event):
    # textString = textField.get(1.0, "end")
    # textField.configure(height=textString.count('\n'))
    # count = textString.count('\n')
    root.after(200, lambda: configureTextField(event))

textFieldHeight = 1

def configureTextField(event):
    global textFieldHeight
    if event.keysym == 'Return' or event.keysym == 'BackSpace':
        textString = textField.get(1.0, "end")
        textString = textString[:-1]
        startLength = len(textString)
        if len(textString) > 0:
            if textString[0] == '\n':
                textString = textString[1:]
            if len(textString) > 1:
                if textString[-1] == '\n':
                    if textString[-2] == '\n':
                        textString = textString[:-1]
        # textString = replaceDoubleNewLine(textString)
        if len(textString) != startLength or textString.count('\n') + 1 != textFieldHeight:
            textField.delete(0.0, tk.END)
            textField.insert(tk.INSERT, textString)
            textField.configure(height=textString.count('\n') + 1)
            textField.update()
            textFieldHeight = textString.count('\n') + 1
def updateTextField(event):
    textString = textField.get(1.0, "end")
    textString = textString[:-1]
    if len(textString) > 0:
        if textString[0] == '\n':
            textString = textString[1:]
        if len(textString) > 1:
            if textString[-1] == '\n':
                if textString[-2] == '\n':
                    textString = textString[:-1]
    textString = replaceExtraNewLine(textString)
    textField.delete(0.0, tk.END)
    textField.insert(tk.INSERT, textString)
    textField.configure(height=textString.count('\n') + 1)
    textField.update()
def testTextField(arg):
    if textField.get()[:-1] == '':
        return False
    else:
        return True

def flood():
    global parsedId
    updateTextField("sd")
    if justTestIdEntry() and testRequestsEntry("ff") and testThreadsEntry("ff"):
        textToSend = textField.get(1.0, "end")
        textToSend = replaceExtraNewLine(textToSend)
        textToSend = textToSend[:-1]
        votes = textToSend.split('\n')

        print("Executing: " + str(parsedId))
        Bot(parsedId, votes, eval(threadsEntry.get()), eval(requestsEntry.get()), perWord.get()) # TODO: perWord is never changed

def testIdEntry():
    textField.focus_set()

def justTestIdEntry():
    inputId = idEntry.get()
    if inputId == '':
        idOk.grid_remove()
        idNotFound.grid(row=0, column=2)
        idTesting.update()
        idEntry.focus_set()
        return False
    else:
        idOk.grid_remove()
        idOk.update()
        idNotFound.grid_remove()
        idNotFound.update()
        idTesting.grid(row=0, column=2)
        idTesting.update()
        global parsedId
        try:
            s = requests.get('https://www.menti.com/core/objects/vote_ids/'+str(inputId))
            if s.json()['code'] == 'not_found':
                idOk.grid_remove()
                idTesting.grid_remove()
                idNotFound.grid(row=0, column=2)
                idEntry.focus_set()
                return False
            else:
                idTesting.grid_remove()
                idOk.grid(row=0, column=2)
                idNotFound.grid_remove()
                textField.focus_set()
                parsedId = s.json()['id']
                return True
        except KeyError as e:
            idTesting.grid_remove()
            idOk.grid(row=0, column=2)
            idNotFound.grid_remove()
            textField.focus_set()
            parsedId = s.json()['id']
            return True
        except Exception as e:
            print("important error")
            print(e)
            idOk.grid_remove()
            idTesting.grid_remove()
            idNotFound.grid(row=0, column=2)
            idEntry.focus_set()
            return False
def testIdEntryBond(event):
    inputId = idEntry.get()
    if inputId == '':
        idOk.grid_remove()
        idNotFound.grid(row=0, column=2)
        idTesting.update()
        idEntry.focus_set()
        return False
    else:
        idOk.grid_remove()
        idOk.update()
        idNotFound.grid_remove()
        idNotFound.update()
        idTesting.grid(row=0, column=2)
        idTesting.update()
        global parsedId
        try:
            s = requests.get('https://www.menti.com/core/objects/vote_ids/'+str(inputId))
            if s.json()['code'] == 'not_found':
                idOk.grid_remove()
                idTesting.grid_remove()
                idNotFound.grid(row=0, column=2)
                idEntry.focus_set()
                return False
            else:
                idTesting.grid_remove()
                idOk.grid(row=0, column=2)
                idNotFound.grid_remove()
                textField.focus_set()
                parsedId = s.json()['id']
                return True
        except KeyError as e:
            idTesting.grid_remove()
            idOk.grid(row=0, column=2)
            idNotFound.grid_remove()
            textField.focus_set()
            parsedId = s.json()['id']
            return True
        except Exception as e:
            print("important error")
            print(e)
            idOk.grid_remove()
            idTesting.grid_remove()
            idNotFound.grid(row=0, column=2)
            idEntry.focus_set()
            return False

def testRequestsEntry(arg):
    if requestsEntry.get() == '':
        requestsEntry.focus_set()
        return False
    else:
        threadsEntry.focus_set()
        return True

def testThreadsEntry(arg):
    if threadsEntry.get() == '':
        threadsEntry.focus_set()
        return False
    else:
        return True

vcmd = (root.register(validate), '%d', '%P')

tk.Label(root, text="id: ").grid(row=0)
tk.Label(root, text="Text to send: ").grid(row=2)

idEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")
idEntry.bind('<Return>', testIdEntryBond)
idEntry.bind('<FocusOut>', testIdEntryBond)
# testIdBtn = tk.Button(root, text='test', command=testIdEntry)
idOk = tk.Label(root, text="OK", fg="#00ff00")
idNotFound = tk.Label(root, text="Not found", fg="#ff0000")
idTesting = tk.Label(root, text="Testing...", fg="#fca503")
textField = tk.Text(root, height=1, width=30, highlightthickness='0', borderwidth=2, relief="sunken")
textField.bind("<KeyRelease>", resizeTextField)
textField.bind("<FocusOut>", updateTextField)


idEntry.grid(row=0, column=1)
idEntry.focus_set()
# testIdBtn.grid(row=0, column=2)
textField.grid(row=2, column=1)

tk.Label(root, text="Requests: ").grid(row=3)
tk.Label(root, text="Threads: ").grid(row=4)

requestsEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")
threadsEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")
perWordView = tk.Checkbutton(root, text="Requests per word?", onvalue = True, offvalue = False, height=5, width = 20, var=perWord)
perWord.set(True)

requestsEntry.bind('<Return>', testRequestsEntry)
# requestsEntry.bind('<FocusOut>', testRequestsEntry)

threadsEntry.bind('<Return>', testThreadsEntry)
# threadsEntry.bind('<FocusOut>', testThreadsEntry)

requestsEntry.grid(row=3, column=1)
threadsEntry.grid(row=4, column=1)
perWordView.grid(row=5, column=2)


tk.Button(root,
          text='flood', command=flood).grid(row=5, column=1)

tk.mainloop()

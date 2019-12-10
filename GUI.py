import tkinter as tk
import requests

parsedId = ""

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
def configureTextField(event):
    if event.keysym == 'Return' or event.keysym == 'BackSpace':
        textString = textField.get(1.0, "end")
        textString = textString[:-1]
        if len(textString) > 0:
            if textString[0] == '\n':
                textString = textString[1:]
            if len(textString) > 1:
                if textString[-1] == '\n':
                    if textString[-2] == '\n':
                        textString = textString[:-1]
        textString = replaceDoubleNewLine(textString)
        textField.delete(0.0, tk.END)
        textField.insert(tk.INSERT, textString)
        textField.configure(height=textString.count('\n') + 1)
        textField.update()
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

def flood():
    updateTextField("sd")
    textToSend = textField.get(1.0, "end")
    textToSend = replaceExtraNewLine(textToSend)
    textToSend = textToSend[:-1]
    votes = textToSend.split('\n')
def testIdEntry():
    inputId = idEntry.get()
    global parsedId
    try:
        s = requests.get('https://www.menti.com/core/objects/vote_ids/'+str(inputId))
        if s.json()['code'] == 'not_found':
            idOk.grid_remove()
            idNotFound.grid(row=1, column=1)
            idEntry.focus_set()
        else:
            idOk.grid(row=1, column=1)
            idNotFound.grid_remove()
            textField.focus_set()
            parsedId = s.json()['id']
    except KeyError:
        idOk.grid(row=1, column=1)
        idNotFound.grid_remove()
        textField.focus_set()
def testIdEntryBond(event):
    inputId = idEntry.get()
    idOk.grid_remove()
    idOk.update()
    idNotFound.grid_remove()
    idNotFound.update()
    idTesting.grid(row=1, column=1)
    idTesting.update()
    try:
        s = grequests.get('https://www.menti.com/core/objects/vote_ids/'+str(inputId))
        if s.json()['code'] == 'not_found':
            idOk.grid_remove()
            idTesting.grid_remove()
            idNotFound.grid(row=1, column=1)
            idEntry.focus_set()
        else:
            idTesting.grid_remove()
            idOk.grid(row=1, column=1)
            idNotFound.grid_remove()
            textField.focus_set()
    except KeyError:
        idTesting.grid_remove()
        idOk.grid(row=1, column=1)
        idNotFound.grid_remove()
        textField.focus_set()
    except Exception:
        idOk.grid_remove()
        idTesting.grid_remove()
        idNotFound.grid(row=1, column=1)
        idEntry.focus_set()

root = tk.Tk()

vcmd = (root.register(validate), '%d', '%P')

tk.Label(root, text="id: ").grid(row=0)
tk.Label(root, text="Text to send: ").grid(row=2)

idEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")
idEntry.bind('<Return>', testIdEntryBond)
idEntry.bind('<FocusOut>', testIdEntryBond)
testIdBtn = tk.Button(root, text='test', command=testIdEntry)
idOk = tk.Label(root, text="OK", fg="#00ff00")
idNotFound = tk.Label(root, text="Not found", fg="#ff0000")
idTesting = tk.Label(root, text="Testing...", fg="#fca503")
textField = tk.Text(root, height=1, width=30, highlightthickness='0', borderwidth=2, relief="sunken")
textField.bind("<KeyRelease>", resizeTextField)
textField.bind("<FocusOut>", updateTextField)

idEntry.grid(row=0, column=1)
idEntry.focus_set()
testIdBtn.grid(row=0, column=2)
textField.grid(row=2, column=1)


# threadsEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")
# requestsEntry = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness=0, borderwidth=2, relief="sunken")



tk.Button(root,
          text='flood', command=flood).grid(row=3, column=1)

tk.mainloop()

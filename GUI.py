import tkinter as tk
import requests

def validate(action, value_if_allowed):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return True

def flood():
    # print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    pass
def testId():
    inputId = idField.get()
    try:
        pass
    except KeyError:
        pass
    s = requests.get('https://www.menti.com/core/objects/vote_ids/'+str(input))
    parsedId = s.json()['id']

root = tk.Tk()

vcmd = (root.register(validate), '%d', '%P')

tk.Label(root, text="id: ").grid(row=0)
tk.Label(root, text="Last Name").grid(row=1)

idField = tk.Entry(root, validate='key', validatecommand=vcmd, width=23, highlightthickness='0', borderwidth=2, relief="sunken")
testIdBtn = tk.Button(root, text='test', command=testId)
textField = tk.Text(root, height=2, width=30, highlightthickness='0', borderwidth=2, relief="sunken")

idField.grid(row=0, column=1)
testIdBtn.grid(row=0, column=2)
textField.grid(row=1, column=1)

tk.Button(root,
          text='flood', command=flood).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()

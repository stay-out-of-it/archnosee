import tkinter

top = tkinter.Tk()

c = []
def saveCallback():
    global c
    c += [e1.get()]


e1 = tkinter.Entry(top)
b1 = tkinter.Button(top, text ="Save", command = saveCallback)

e1.pack(side=tkinter.LEFT)
b1.pack(side=tkinter.RIGHT)

top.mainloop()

print(c)

from Tkinter import Tk,Button,StringVar,Entry,Label
import random, tkFileDialog, tkMessageBox
root= Tk()
root.wm_title("Random Student Selector")
current=StringVar()
kids=[]
addKidName=Entry(root)
def addkid():
    kids.append(addKidName.get())
addKid=Button(root, text="Add a student", command=addkid)
def choosekid():
    try:
        chosen=random.choice(kids)
    except IndexError:
        tkMessageBox.showinfo("Empty class", "You need to add a student")
    current.set(chosen)
chooseKid=Button(root,text="Pick random student", command=choosekid)
chosenKid=Label(root,textvariable=current)
def loadfile():
    global kids
    loadedfile=tkFileDialog.askopenfile(mode='r', filetypes=[("Text files","*.ssc")])
    try:
        kids=loadedfile.read().split(",")
    except AttributeError:
        tkMessageBox.showinfo("No file selected", "You need to select a file")
loadFile=Button(root,text="Load a class",command=loadfile)
def savetofile():
    savefile=tkFileDialog.asksaveasfile()
    stringToSave=""
    for i in kids:
        stringToSave=stringToSave+i+","
    stringToSave=stringToSave[:-1]
    savefile.write(stringToSave)
saveToFile=Button(root,text="Save a file",command=savetofile)
addKid.grid(row=0,column=1)
addKidName.grid(row=0,column=0)
chooseKid.grid(row=1,column=1)
chosenKid.grid(row=1,column=0)
loadFile.grid(row=2,column=0)
saveToFile.grid(row=2,column=1)
root.mainloop()

from tkinter import *
root = Tk()
root.geometry("500x300")
root.resizable(0,0)
var1 = StringVar()

def myfun():
    var1.set('hello world')



e1 = Entry(textvariable=var1)
e1.place(x = 70, y = 10)

b = Button(text ="Submit",bg = 'green',command=lambda : myfun()).place(x = 14,y = 30)

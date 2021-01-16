from tkinter import *
from functools import partial

def details(a,b,l):
    x = a.get()
    y = b.get()
    l1.config(text = x)
    l2.config(text = y)

root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Registration form")
Label(root, text = "REGISTRATION FORM").place(x = 80,y = 10)
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

name = Label(root,text = "name").place(x = 30, y = 40)
Ph_no = Label(root,text = "Phone Number").place(x = 30, y = 70)
gender = Label(root,text = "Gender").place(x = 30, y = 100)
email = Label(root,text = "E-mail").place(x = 30, y = 130)

l1 = Label()
l1.place(x = 30,y = 150)
l2 = Label()
l2.place(x = 30,y = 170)

nameentry = Entry(root, textvariable = var1).place(x = 130,y = 40)
ph_noentry = Entry(root, textvariable = var2).place(x = 130, y = 70)
genderentry = Entry(root, textvariable = var3).place(x = 130, y = 100)
emailentry = Entry(root, textvariable = var4).place(x = 130, y = 130)

data = partial(details,var1,var2,l1)

b = Button(text="Submit",height = 5,width = 5,bg="yellow",fg="red",activebackground='orange',command = data)
b.place(x= 150, y = 150)



root.mainloop()
print(var1.get())
print(var2.get())
print(var3.get())
print(var4.get())
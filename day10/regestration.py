from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Registration form")
Label(root, text = "REGISTRATION FORM").grid(row = 0,column = 2,columnspan = 5

name = Label(root,text = "name")
Ph_no = Label(root,text = "Phone Number")
gender = Label(root,text = "Gender")
email = Label(root,text = "E-mail")

name.grid(row = 1,column = 2)
Ph_no.grid(row = 2,column = 2)
gender.grid(row = 3,column = 2)
email.grid(row = 4,column = 2)
nameentry = Entry(root)
ph_noentry = Entry(root)
genderentry = Entry(root)
emailentry = Entry(root)

nameentry.grid(row = 1,column = 3)
ph_noentry.grid(row = 2,column = 3)
genderentry.grid(row = 3,column = 3)
emailentry.grid(row = 4,column = 3)

b = Button(text="Submit",bg="yellow",fg="red",activebackground='orange')
b.grid(row = 5,column = 2,columnspan = 5)

root.mainloop()
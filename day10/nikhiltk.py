from tkinter import *
w = Tk() #create a window
w.geometry('300x300+500+100')
w.title('Tkinter App')
b = Button(text="Submit",height = 5,width = 5,bg="yellow",fg="red",activebackground='orange')
b.pack()
b2 = Button(text = "login",bg='red')
b2.pack(side=TOP,fill='x')
b3 = Button(text = "click1",bg='orange')
b3.pack(side=LEFT,fill='y')
b4 = Button(text = "click2",bg='blue')
b4.pack(side=RIGHT,fill='y')
b5 = Button(text = "click3",bg='green')
b5.pack(side=BOTTOM,fill='x')
l = Label(text="Hello World")
l.pack()
Entry().pack()
w.mainloop()
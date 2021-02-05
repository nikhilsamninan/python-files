from tkinter import *
from functools import partial


root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Calculator")
var1 = StringVar()

# functions
def button_click(number):           #to concate the number first enter and 2nd
    s = var1.get()
    var1.set(str(s)+str(number))

def process():                      #to do all the process
    first_number = var1.get()
    var1.set(eval(first_number))

def clear():
    var1.set("")   #to clear the value



# assign entry 

entry = Entry(root,width = 60,textvariable = var1)
entry.grid(row=0,column=0,padx=10,pady=10,columnspan=20)

#Assigning buttons for numbers

button_1 = Button(root, text="1",padx=40, pady=10, command=lambda: button_click(1),bg="black",fg="white")
button_2 = Button(root, text="2",padx=40, pady=10, command=lambda: button_click(2),bg="black",fg="white")
button_3 = Button(root, text="3",padx=40, pady=10, command=lambda: button_click(3),bg="black",fg="white")

button_4 = Button(root, text="4",padx=40, pady=10, command=lambda: button_click(4),bg="black",fg="white")
button_5 = Button(root, text="5",padx=40, pady=10, command=lambda: button_click(5),bg="black",fg="white")
button_6 = Button(root, text="6",padx=40, pady=10, command=lambda: button_click(6),bg="black",fg="white")

button_7 = Button(root, text="7",padx=40, pady=10, command=lambda: button_click(7),bg="black",fg="white")
button_8 = Button(root, text="8",padx=40, pady=10, command=lambda: button_click(8),bg="black",fg="white")
button_9 = Button(root, text="9",padx=40, pady=10, command=lambda: button_click(9),bg="black",fg="white")

button_0 = Button(root, text="0",padx=40, pady=10, command=lambda: button_click(0),bg="black",fg="white")

#Assigning buttons for operators

button_add = Button(root, text="+",padx=40, pady=10,command=lambda: button_click("+"),bg="#343b3b",fg="white")
button_subtract = Button(root, text="-",padx=41, pady=10,command=lambda: button_click("-"),bg="#343b3b",fg="white")
button_multiply = Button(root, text="x",padx=40, pady=10,command=lambda: button_click("*"),bg="#343b3b",fg="white")
button_divide = Button(root, text="÷",padx=40, pady=10,command=lambda: button_click("/"),bg="#343b3b",fg="white")
button_equal = Button(root, text="=",padx=40, pady=10,command=process)
#Assigning other buttons

button_clear = Button(root, text="C",padx=40, pady=10,command=clear,bg="#343b3b",fg="white")

#placing buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2,)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2,)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2,)

button_multiply.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_divide.grid(row=4,column=2)

button_clear.grid(row=1,column=4)
button_add.grid(row=2,column=4)
button_subtract.grid(row=3,column=4,columnspan=67)
button_equal.grid(row=4,column=4)


root.mainloop()
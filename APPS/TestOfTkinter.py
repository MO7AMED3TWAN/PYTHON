###IMPORTING####
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from pyparsing import White
####creat the main app####
test = Tk()
####change title####
test.title("Test APP")
####set dimension####
test.geometry("400x600")
test.minsize(400,600)
test.maxsize(400,600)

####write test label####

label1=Label(test,text="WELCOME",height=1,font=("Arial",20))#.pack()ممكن تكتبها هنا او زى ال تحت 
label1.pack()#put text into main window


####create entry label####

name=Entry(test,width=30,borderwidth=5)
name.pack()
#insert text into entry box 
name.insert(0,"Enter your name")

####my functions#### 
def myClick():
    Hello="Hello "+ name.get()
    my_label=Label(test,text=Hello).pack()

####creat buttons####

#padx,pady is dimension of button
#command is used to make a specific job and take a function in it 
#fg is to color the text
#bg is to color the buttons

btn1=Button(test,text="Click Me!",padx=40,pady=8,command=myClick,bg="#34548a",fg="white").pack()


#$$$$run infintly$$$$
test.mainloop()   

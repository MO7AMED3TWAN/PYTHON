#importing
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from turtle import color

from pyparsing import White
#Functions
def calc():
    #get age in years
    age_years=int(age.get())
    age_months=age_years*12
    age_weeks=age_months*4
    age_days=age_years*365

    line1=f"UR AGE IN MONTHS IS : {age_months}"
    line2=f"UR AGE IN WEEKS  IS : {age_weeks}"
    line3=f"UR AGE IN DAYS   IS : {age_days}"
    all_lines=[line1,line2,line3]
    
    messagebox.showinfo("UR AGE IN ALL UNITS","\n".join(all_lines))

#creat the main App window
age_app=Tk()
#creat title for window
age_app.title("Mo7amed Saied Calculate Age App")
#Set Dimension
age_app.geometry("400x480")
#write label
age_label=Label(age_app,text="WELCOME\n Write UR AGE \n",height=3,font=("Arial",40))
age_label.pack()#put it in main window
#Age variable
age = StringVar()
#Set defult value for age
age.set("0000")
#creat input label for age
age_input=Entry(age_app,width=2,font=("Arial",20),textvariable=age)
age_input.pack()
#creat calc button 
btn=Button(age_app,text=("CALC AGE"),font=("Arial",18),width=20,height=2,bg="#e91e63",
            fg="black",borderwidth=3,command=calc)
btn.pack()


#Run Infinitely
age_app=mainloop()

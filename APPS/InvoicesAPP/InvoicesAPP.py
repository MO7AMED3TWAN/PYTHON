 ###IMPORTING###
from cProfile import label
from tkinter import *
import sqlite3
from tkinter.ttk import Panedwindow
from matplotlib.pyplot import get

from pyparsing import col




####creat the main app####
database = Tk()
####change title####
database.title("INVOICES App")
####set dimension####
database.geometry("480x540")
database.minsize(480,540)#حد التصغير 
database.maxsize(480,740)#حدالتكبير
database.attributes('-alpha',0.8)#الشفافيه
###creation functions ###
def submit():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('InvoisesApp.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create submit query
    c.execute ("INSERT INTO Invoices VALUES (:context,:price,:phonenumber,:name) ",
        {'context':context.get(),
         'price':price.get(),
         'phonenumber':pnumber.get(),
         'name':name.get()
        }  
    
     )
     
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    
 
def show():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('InvoisesApp.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create show query
   # c.execute("DELETE FROM Invoices")
    c.execute ("SELECT *,oid FROM Invoices")
    records = c.fetchall()
    print(records)#print it in terminal
    
    #show it in ur app
    one_line=''
    for record in records:
        one_line += f"ID : {str(record[4])}" +"|||"+f"CONTEXT : {str(record[0])}" +"|||"+f"PRICE : {str(record[1])}"+"|||"+f"PHONE NUMBER : {str(record[2])}" +"|||"+f"NAME : {str(record[3])}" + "\n" 
    global newWindow
    newWindow=Toplevel(database)#تعريف الويندو الجديده
    newWindow.title("Invoices Details")#عنوان الويندو الجديده
    newWindow.minsize(880,750)#حد التصغير 
    newWindow.maxsize(1360,750)#حدالتكبير
    newWindow.attributes('-alpha',0.9)#الشفافيه  
    newWindow.geometry("480x740")#احداثيات الويندو الجديده
    one_line_label=Label(newWindow,text=one_line).pack()#لاظهار الويندو
    




def delete():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('InvoisesApp.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create delete query
    c.execute("DELETE FROM Invoices WHERE oid= "+ delete_box.get())

    newWindow.destroy()

    #commit changes
    conn.commit()
    #close connection
    conn.close()
    


####create adatabase &connect to one####
conn=sqlite3.connect('InvoisesApp.db')

####create a cursor####
c =conn.cursor()
'''
####Create Tables####
c.execute ("""CREATE TABLE Invoices 
(
    context text NOT NULL,
    price NOT NULL,
    phonenumber NOT NULL,
    name taxt NOT NULL
)
""")
'''
####create entry labels####
context =Entry(database,width=40,borderwidth=5)
context.grid(row=0,column=1)
context_label=Label(database,text="CONTEXT")
context_label.grid(row=0,column=0)

price =Entry(database,width=40,borderwidth=5)
price.grid(row=1,column=1)
price_label=Label(database,text="PRICE")
price_label.grid(row=1,column=0)

pnumber =Entry(database,width=40,borderwidth=5)
pnumber.grid(row=2,column=1)
pnumber_label=Label(database,text="PHONE NUMBER")
pnumber_label.grid(row=2,column=0)

name =Entry(database,width=40,borderwidth=5)
name.grid(row=3,column=1)
name_label=Label(database,text="NAME")
name_label.grid(row=3,column=0)


delete_box=Entry(database,width=40)
delete_box.grid(row=6,column=1)
delete_box_label=Label(database,text="DELETE BY ' ID,NAME,PHONE NUMBER '")
delete_box_label.grid(row=6,column=0)

####create submit button####
submit_btn=Button(database,text="ADD NEW INVOICE",command=submit)
submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=40,ipadx=100)
####create show button####
show_btn=Button(database, text="SHOW INVOCES",command=show)
show_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=40,ipadx=100)
show_btn.update_idletasks()
####create delete button####
delete_btn=Button(database,text="DELETE !!!",command=delete)
delete_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=40,ipadx=50)

















#commit changes
conn.commit()
#close connection
conn.close()
#$$$$run infintly$$$$
database.mainloop()  

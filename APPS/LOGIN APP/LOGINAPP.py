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
database.title("DATABASE LOGIN APP")
####set dimension####
database.geometry("480x540")
database.minsize(480,540)#حد التصغير 
database.maxsize(480,740)#حدالتكبير
database.attributes('-alpha',0.9)#الشفافيه
###creation functions ###
def submit():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('login-page.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create submit query
    c.execute ("INSERT INTO Acounts VALUES (:id,:username,:password) ",
        {'id':id.get(),
         'username':username.get(),
         'password':password.get()
        }  
    
     )
     
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    
    #clear text box
    id.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)


def show():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('login-page.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create show query
   # c.execute("DELETE FROM Acounts")
    c.execute ("SELECT *,oid FROM Acounts")
    records = c.fetchall()
    print(records)#print it in terminal
    #show it in ur app

    one_line=''
    for record in records:
        one_line += f"ID : {str(record[3])}" +"|||"+f"USERNAME : {str(record[1])}" +"|||"+f"PASSWORD : {str(record[2])}" + "\n"
    global newWindow
    newWindow=Toplevel(database)#تعريف الويندو الجديده
    newWindow.title("Accounts Details")#عنوان الويندو الجديده
    newWindow.minsize(480,540)#حد التصغير 
    newWindow.maxsize(480,840)#حدالتكبير
    newWindow.attributes('-alpha',0.9)#الشفافيه  
    newWindow.geometry("480x740")#احداثيات الويندو الجديده
    one_line_label=Label(newWindow,text=one_line).pack()#لاظهار الويندو
    




def delete():
    ####create adatabase &connect to one####
    conn=sqlite3.connect('login-page.db')

    ####create a cursor####
    c =conn.cursor()
    
    #create delete query
    c.execute("DELETE FROM Acounts WHERE oid= "+ delete_box.get())

    
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    
    #clear text box
    id.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)

    newWindow.destroy()


####create adatabase &connect to one####
conn=sqlite3.connect('login-page.db')

####create a cursor####
c =conn.cursor()
'''
####Create Tables####
c.execute ("""CREATE TABLE Acounts 
(
    id integer,
    username text,
    password text
)
""")
'''
####create entry labels####
id =Entry(database,width=40,borderwidth=5)
id.grid(row=0,column=1)
id_label=Label(database,text="ID")
id_label.grid(row=0,column=0)

username =Entry(database,width=40,borderwidth=5)
username.grid(row=1,column=1)
username_label=Label(database,text="USERNAME")
username_label.grid(row=1,column=0)

password =Entry(database,width=40,borderwidth=5)
password.grid(row=2,column=1)
password_label=Label(database,text="PASSWORD")
password_label.grid(row=2,column=0)

delete_box=Entry(database,width=40)
delete_box.grid(row=6,column=1)
delete_box_label=Label(database,text="DELETE ID")
delete_box_label.grid(row=6,column=0)

####create submit button####
submit_btn=Button(database,text="ADD NEW USER",command=submit)
submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=40,ipadx=100)
####create show button####
show_btn=Button(database, text="SHOW ACCOUNTS",command=show)
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

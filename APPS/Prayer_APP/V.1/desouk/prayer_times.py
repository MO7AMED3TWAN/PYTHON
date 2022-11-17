###IMPORTING###
from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup as S


#API
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
req=requests.get('https://timesprayer.com/en/prayer-times-in-desouk-city.html',headers=headers)
soup=S(req.content,'html.parser')
obj=soup.find(class_="info prayertable mobile").find_all('li')
 

#make window
test = Tk()
test.title("PRAYER TIMES AT DESOUQ")
test.geometry("450x700")
test.minsize(450,700)
test.maxsize(450,700)

#current time
now = datetime.now()
time_now=now.strftime("%I:%M %p")

####write test label####
l1=Label(test,text='',height=1,font=("Arial",10)).pack()
title=Label(test,text="مواقيت الصلاة فى دسوق",height=2,font=("ِArial",30),relief="raised",bd=10,fg='#E7EAEF',bg='#37745B').pack()
l2=Label(test,text='',height=1,font=("Arial",10)).pack()
l3=Label(test,text=f"TIME NOW : {time_now}",font=("Arial",20),fg='#EE3B3B',relief="sunken").pack()
l4=Label(test,text='',height=1,font=("Arial",10)).pack()
l5=Label(test,text=obj[0].text,height=1,font=("Arial",40),fg='#02315E').pack()
l6=Label(test,text=obj[2].text,height=1,font=("Arial",40),fg='#00457E').pack()
l7=Label(test,text=obj[3].text,height=1,font=("Arial",40),fg='#2F70AF').pack()
l8=Label(test,text=obj[4].text,height=1,font=("Arial",40),fg='#B9848C').pack()
l9=Label(test,text=obj[5].text,height=1,font=("Arial",40),fg='#806491').pack()
l10=Label(test,text='',height=1,font=("Arial",10)).pack()
exit_button=Button(test,text="QUIT",height=1,font=("ِArial",20),command=test.destroy,relief="raised",bd=10,fg='#E7EAEF',bg='#37745B').pack()


#$$$$run infintly$$$$
test.mainloop()   





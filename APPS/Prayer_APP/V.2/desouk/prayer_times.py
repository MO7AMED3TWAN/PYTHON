###IMPORTING###
from tkinter import *
from datetime import datetime
from urllib import request
import requests
from playsound import playsound as play
from bs4 import BeautifulSoup as S
from random import randint
import json

#API
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
req=requests.get('https://timesprayer.com/en/prayer-times-in-desouk-city.html',headers=headers)
soup=S(req.content,'html.parser')
obj=soup.find(class_="info prayertable mobile").find_all('li')


import json
url = 'http://api.aladhan.com/v1/timingsByCity?city=Alexandria&country=Egypt'
html = requests.get(url).content
soup = S(html,'html.parser')
site_json=json.loads(soup.text)
timings = list(site_json['data']['timings'].values())[0:7]
f=timings[0]
d=timings[2]
asr=timings[3]
mag=timings[5]
ish=timings[6]

print(f,d,asr,mag,ish)


#make window

test = Tk()
test.title("PRAYER TIMES AT DESOUQ")
test.geometry("450x700")
test.minsize(450,700)
test.maxsize(450,700)

 

####write test label####
l1=Label(test,text='',height=1,font=("Arial",10)).pack()
title=Label(test,text="مواقيت الصلاة فى دسوق",height=2,font=("ِArial",30),relief="raised",bd=10,fg='#E7EAEF',bg='#37745B').pack()
l2=Label(test,text='',height=1,font=("Arial",10)).pack()
##################
l3= Label(test,text="TIME NOW :",height=1,font=("Arial",20),fg='#02315E')
l3.pack()




#current time
def updateTime():
    currentime = datetime.now()
    hours = currentime.strftime('%H')
    minutes = currentime.strftime('%M')
    seconds = currentime.strftime('%S')
    mixed = currentime.strftime('%I:%M')
    l3.configure(text=f"TIME NOW : {mixed}")
    for i in range(len(timings)):
        timePray = timings[i]
        timeNow = str(mixed).lstrip('0')
        if(timeNow == timePray):
            play('mixkit-doorbell-single-press-333.wav')
        else:
            print(timePray)
            print(timeNow)
    test.after(1000 ,updateTime)

updateTime()


##################
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


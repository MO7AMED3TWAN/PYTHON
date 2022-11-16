from tkinter import *
from pytube import YouTube
import pytube

#creation main window
downloader=Tk()
downloader.title("DOWNLOAD FROM YOUTUBE")
downloader.geometry("340x400")
downloader.minsize(340,400)
downloader.maxsize(340,400)

Label(downloader,text="ENTER URL HERE",font=("Arial",20)).grid(row=0,column=1)

url=StringVar()
url_enter=Entry(downloader,width=40,borderwidth=10,textvariable=url)
url_enter.grid(row=2,column=1)

def downloadA():
    link =YouTube(str(url.get())).streams.get_audio_only().download(r'C:\Users\MoHaMeD\Desktop\Desktop')
    Label(downloader, text = 'DOWNLOADED AUDIO', font = 'arial 15').place(x= 70 , y = 300)
Button(downloader, text = "DOWNLOAD AUDIO",padx=60,pady=10,bg="#34548a",fg="white",command = downloadA).place(x=40,y=120)

def downloadV():
    x=pytube.YouTube(str(url.get())).streams.get_highest_resolution().download(r'C:\Users\MoHaMeD\Desktop\Desktop')
    Label(downloader, text = 'DOWNLOADED VIDEO', font = 'arial 15').place(x= 90 , y = 300)
Button(downloader,text="DOWNLOAD VIDEO",padx=60,pady=10,bg="#34548a",fg="white",command=downloadV).place(x=43,y=200)

downloader.mainloop()
import tkinter as tk
from tkinter import *
import playsound as p
from playsound import *
window = Tk()
window.geometry("250x50")
window.title("Sound-bar")
window.config(background="yellow")
def bark():
    playsound("barking_small.mp3")
def beep():
    playsound("censor-beep-1.mp3")
def yipee():
    playsound("yippee-tbh.mp3")
def pew():
    playsound("pew_pew-dknight556-1379997159.mp3")
def crack():
    playsound("bone-crack.mp3")
l1 = Label(window,text="Click a sound :)")
bbark = Button(window,width=5,text="bark",command=bark)
bbeep = Button(window,width=5,text="*beeP*",command=beep)
byipee = Button(window,width=5,text="YIPEE",command=yipee)
bpew = Button(window,width=5,text="pew",command=pew)
bcrack = Button(window,width=5,text="cRACk",command=crack)
l1.grid(row=1,column=1,columnspan=2)
bbark.grid(row=2,column=1)
bbeep.grid(row=2,column=2)
byipee.grid(row=2,column=3)
bpew.grid(row=2,column=4)
bcrack.grid(row=2,column=5)
window.mainloop()
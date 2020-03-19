# script heure.py
from tkinter import *
import os

def radio1():
    os.system('sudo killall mplayer')
    os.system('mplayer http://streamingp.shoutcast.com/NRJ &')

def radio2():
    os.system('sudo killall mplayer')
    os.system('mplayer http://ais-live.cloud-services.paris:8000/virgin.mp3 &')

def radio3():
    os.system('sudo killall mplayer')
    os.system('mplayer    http://streaming.radio.rtl.fr/rtl-1-48-192 &')

def radio4():
    os.system('sudo killall mplayer')
    os.system('mplayer http://cdn.nrjaudio.fm/audio1/fr/30201/mp3_128.mp3?origine=fluxradios &')

def radio5():
    os.system('sudo killall mplayer')
    os.system('mplayer http://target-ad-2.cdn.dvmr.fr/ouifm-high.mp3 &')

def radio6():
    os.system('sudo killall mplayer')
    os.system('mplayer     http://direct.franceinfo.fr/live/franceinfo-midfi.mp3 &')
    
def radio7():
    os.system('sudo killall mplayer')
    os.system('mplayer http://rfm-live-mp3-128.scdn.arkena.com/rfm.mp3 &')
    
def radio8():
    os.system('sudo killall mplayer')
    os.system('mplayer http://cdn.nrjaudio.fm/audio1/fr/30601/mp3_128.mp3?origine=fluxradios &')

def radio9():
    os.system('sudo killall mplayer')
    os.system('mplayer http://streaming.radio.funradio.fr/fun-1-48-192 &')
    
def radio10():
    os.system('sudo killall mplayer')
    os.system('mplayer http://streaming.radio.rtl2.fr/rtl2-1-48-192 &')
    
def radio11():
    os.system('sudo killall mplayer')
    root.destroy()
    
def radio12():
    root.destroy()
    
root = Tk()
#root.geometry('700x350')
root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Heure courante")

heure = StringVar()
Label(root,textvariable=heure).place(x=350,y=175)


Bouton1 = Button(root, text = 'NRJ', command = radio1,height = 3, width = 10).place(x=1,y=1)
Bouton2 = Button(root, text = 'Virgin Radio',command = radio2,height = 3, width = 10).place(x=100,y=1)
Bouton3 = Button(root, text = 'RTL', command = radio3,height = 3, width = 10).place(x=200,y=1)
Bouton4 = Button(root, text = 'Cherie FM', command = radio4,height = 3, width = 10).place(x=300,y=1)
Bouton5 = Button(root, text = 'OUI FM', command = radio5,height = 3, width = 10).place(x=1,y=90)
Bouton6 = Button(root, text = 'France INFO', command = radio6,height = 3, width = 10).place(x=100,y=90)
Bouton7 = Button(root, text = 'RFM', command = radio7,height = 3, width = 10).place(x=200,y=90)
Bouton8 = Button(root, text = 'Nostalgie', command = radio8,height = 3, width = 10).place(x=300,y=90)
Bouton9 = Button(root, text = 'FUN radio', command = radio9,height = 3, width = 10).place(x=1,y=180)
Bouton10 = Button(root, text = 'RTL2', command = radio10,height = 3, width = 10).place(x=100,y=180)
Bouton11 = Button(root, text = 'Arreter',bg = "red", command = radio11,height = 3, width = 10).place(x=200,y=180)
Bouton12 = Button(root, text = 'Quitter',bg = "red", command = radio12,height = 3, width = 10).place(x=300,y=180)

root.mainloop()

from tkinter import *
import pyttsx3
import pandas as pd
from datetime import *
#import pyttsx3
import webbrowser
from pygame import mixer
import subprocess
from youtube_search import YoutubeSearch
engine = pyttsx3.init()
def speak(text):
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
def send():
    data = pd.read_csv("sources/trainer.csv")
    msg = e.get("1.0",'end-1c').strip()
    out = 0   
    if msg != '':
        t.config(state=NORMAL)
        t.insert(END, "You: " + msg + '\n\n')    
        if "open" in msg.lower() and out==0:
                mg = msg.replace(" ", "").replace("open", "")
                mg = mg.replace(" ", "")
                mg = mg.lower()
                t.insert(END, "Leon: Opening " + mg +".com"+ '\n\n')
                speak("Opening {}.com".format(mg))
                webbrowser.open('{}.com'.format(mg))
                out = 1
        elif "yt" in msg.lower() and out==0:
                mg = msg.replace("yt", "")
                mg = mg.title()
                t.insert(END, "Leon: Playing " + mg +" in youtube.com"+ '\n\n')    
                speak("Playing {} in youtube.com".format(mg))
                results = YoutubeSearch('{}'.format(mg), max_results=10).to_dict()
                for v in results:
                    webbrowser.open('https://www.youtube.com/watch?v=' + v['id'])
                out = 1
        elif "date" in msg.lower() and out==0:
                dt = datetime.now()
                d = dt.strftime("%d")
                m = dt.strftime("%B")
                y = dt.strftime("%Y")
                t.insert(END, "Leon: Today's Date: "+"{} {} {}".format(d,m,y)+ '\n\n')  
                speak("Today's Date is {} {} {}".format(d,m,y))
                out = 1        
        elif "time" in msg.lower() and out==0:
                dt = datetime.now()
                h = dt.strftime("%I")
                m = dt.strftime("%M")
                p = dt.strftime("%p")
                t.insert(END, "Leon: Current Time: "+"{}:{} {}".format(h,m,p)+ '\n\n')  
                speak("Current Time is {} {} {}".format(h,m,p))
                out = 1       
        elif "weather" in msg.lower() and out==0:                
                t.insert(END, "Bot: Looking for " + msg + '\n\n')  
                speak("Opening weather in google.com")
                webbrowser.open('https://www.google.com/search?q={}'.format(msg))
                out = 1       
        elif "music" in msg.lower() and out==0:                
                t.insert(END, "Leon: Playing " + msg + " for you." +'\n\n')  
                speak("Playing Music for you. Enjoy")
                mixer.init()
                mixer.music.load('sources/music/1.mp3')
                mixer.music.play()
                out = 1               
        elif "mstop" in msg.lower() and out==0:                
                t.insert(END, "Leon: Stopping music for you." +'\n\n')
                mixer.music.stop()
                speak("Stopped Muisc for you.")
                out = 1              
        elif "files" in msg.lower() and out==0:                
                t.insert(END, "Leon: Openning File Manager." +'\n\n')
                subprocess.call(["explorer.exe"])
                speak("Openning File Manager for you.")
                out = 1             
        elif "calc" in msg.lower() and out==0:                
                t.insert(END, "Leon: Openning Calculator." +'\n\n')
                subprocess.call(["calc.exe"])
                speak("Openning Calculator for you.")
                out = 1    
        else:
            for i in range(len(data)):
                if data['input'].iloc[i] in msg.lower() and out==0:
                    t.insert(END, "Leon: " + data['output'].iloc[i] + '\n\n')
                    speak(data['output'].iloc[i])
                    out = 1
        t.config(state=DISABLED) 
        t.yview(END)
def About():
        top = Toplevel()
        top.title("About Leon's Developers")
        top.iconbitmap('sources/icon.ico')
        top.geometry("222x160")
        top.resizable(width=FALSE, height=FALSE)
        ta = Text(top, bd=0, height="8", width="50", font="Consolas",)
        ta.config(background="#FFFF9D",foreground="#319981", font=("Consolas", 11, 'bold' ))
        ta.insert(END, ' Crafted by:\n\n')
        ta.insert(END, '\tRahul V\n\tGirish Raj M\n\tHarish M\n')
        ta.insert(END, '~For Python Mini Project~')
        ebot= Button(top, font=("Consolas",11,'bold'), text="CLOSE", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff', command=top.destroy)
        ebot.place(x=80, y=130, height=20, width=60)
        ta.place(x=10,y=10, height=110, width=202, anchor=NW)
def Commands():
        top = Toplevel()
        top.title("Leon's Commands")
        top.iconbitmap('sources/icon.ico')
        top.geometry("300x300")
        top.resizable(width=FALSE, height=FALSE)
        ta = Text(top, bd=0, height="8", width="50", font="Consolas",)
        ta.config(background="#FFFF9D",foreground="#319981", font=("Consolas", 11, 'bold' ))
        ta.insert(END, 'Commands:\n\n')
        ta.insert(END, '  1. open - open name_of_website\n')
        ta.insert(END, '  2. yt - yt keywords_of_video\n')
        ta.insert(END, '  3. date - date\n')
        ta.insert(END, '  4. time - time\n')
        ta.insert(END, '  5. weather - weather\n')
        ta.insert(END, '  6. music - music\n')
        ta.insert(END, '  7. mstop - mstop\n')
        ta.insert(END, '  8. files - files\n')
        ta.insert(END, '  9. calc - calc\n')
        ta.insert(END, '  [commands - syntax]')
        ebot= Button(top, font=("Consolas",11,'bold'), text="CLOSE", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff', command=top.destroy)
        ebot.place(x=110, y=270, height=20, width=60)
        ta.place(x=10,y=10, height=250, width=280, anchor=NW)
        
layout = Tk()
layout.title("Leon: Personal Assistant")
layout.iconbitmap('sources/icon.ico')
layout.geometry("400x560")
layout.resizable(width=FALSE, height=FALSE)
t = Text(layout, bd=0, bg="#fff", height="8", width="50", font="Consolas",)
t.config(background="#FFFF9D",foreground="#319981", font=("Consolas", 11 ))
t.insert(END, "Leon: Hello I'm Leon I'm your personal assistant. How may I help you? "+ '\n\n')
t.config(state=DISABLED)
sb = Scrollbar(layout, command=t.yview)
t['yscrollcommand'] = sb.set
e = Text(layout, bd=0, bg="#fff",width="29", height="3", font="Consolas")
s = Button(layout, font=("Consolas",20,'bold'), text="SEND", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff',command=send)
eb= Button(layout, font=("Consolas",11,'bold'), text="EXIT", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff', command=layout.destroy)
ab= Button(layout, font=("Consolas",11,'bold'), text="ABOUT", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff', command=About)
cb= Button(layout, font=("Consolas",11,'bold'), text="COMMANDS", width="12", height=4,bd=0, bg="#2d5870", activebackground="#2d5870",fg='#fff', command=Commands)
sb.place(x=380,y=0, height=460,width=15)
t.place(x=15,y=15, height=390, width=350)
e.place(x=15, y=420, height=40, width=350)
cb.place(x=18, y=475, height=20, width=110)
eb.place(x=270, y=475, height=20, width=110)
ab.place(x=143, y=475, height=20, width=110)
s.place(x=18, y=505, height=40, width=364)
speak("Hello I'm Leon. I'm your personal assistant. How may I help you ?")
layout.mainloop()




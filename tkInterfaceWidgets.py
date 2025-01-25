#import tkinter as tk #
from tkinter import * #different import process

screen = Tk() # screen name of Tkinter object created
screen.title("Widget Samples") #Screen title defined
screen.minsize(width=300, height=300) #screen size defined

def txt_read(get_txt):
    label.config(text=get_txt)


#Label:
label = Label() #Label object created
label.config(bg="yellow") #label backcolor set yellow
label.config(fg="black") #label foreground color set black
label.config(padx=20,pady=20) #label position pad-x and pad-y

#Button:
button = Button() #new button object created
button.config(text="Resize Form", command=lambda: label.config(text="Try and Catch")) #button click action defined
button.config(bg="yellow") #button backcolor set yellow
button.config(fg="red") #button foreground color set red

#Button2:
btn_text = Button(text="Text Read", command=lambda: txt_read(txt.get("1.0",END))) #get:row1 to END. get:"2.0" to END.

#Text object:
txt = Text(width=30,height=10)


button.pack() #show button
btn_text.pack() #show btn_text
label.pack() #show label
txt.pack() #show text

screen.mainloop()
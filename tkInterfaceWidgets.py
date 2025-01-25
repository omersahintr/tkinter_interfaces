#import tkinter as tk #
from tkinter import * #different import process

screen = Tk() # screen name of Tkinter object created
screen.title("Widget Samples") #Screen title defined
screen.minsize(width=300, height=300) #screen size defined

def txt_read(get_txt):
    label.config(text=get_txt)

def select_scale(value):
    label.config(text = level.get())

def select_spin():
    label.config(text = spin.get())

def select_check():
    label.config(text=IntVar().get())

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
btn_text = Button(text="Text Read", command=lambda: txt_read(txt.get("1.5",END))) #get:row1 to END. get:"2.0" to END.

#Text object:
txt = Text(width=30,height=5)

#Scale:
level = Scale(from_=0, to=100, command = select_scale)

#Spinbox:
spin = Spinbox(from_=0,to=50, command=select_spin)

#Checkbuttom:
check = Checkbutton(text="option-1", variable=IntVar(), command=select_check)


button.pack() #show button
btn_text.pack() #show btn_text
txt.pack() #show text
txt.focus() #txt object on focus
level.pack()
spin.pack()
check.pack() ##
label.pack() #show label

screen.mainloop()
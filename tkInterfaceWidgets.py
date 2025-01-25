#import tkinter as tk
from tkinter import * #different import process

screen = Tk() # screen name of Tkinter object created
screen.title("Widget Samples") #Screen title defined
screen.minsize(width=300, height=300) #screen size defined

label = Label() #Label object created
label.config(bg="yellow") #label backcolor set yellow
label.config(fg="black") #label foreground color set black
label.config(padx=20,pady=20) #label position pad-x and pad-y

button = Button() #new button object created
button.config(text="Resize Form", command=lambda: label.config(text="Try and Catch")) #button click action defined
button.config(bg="yellow") #button backcolor set yellow
button.config(fg="red") #button foreground color set red

button.pack() #show button
label.pack() #show label

screen.mainloop()
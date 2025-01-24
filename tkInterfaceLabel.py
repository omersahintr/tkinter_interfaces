import tkinter as tk

window = tk.Tk() # created tkinter screen.
window.title("First Screen") # Screen title set
window.minsize(width=600,height=600) # window minimum size

#label:
infoLabel = tk.Label(
    text="First Label:")
infoLabel.config(bg="yellow", fg="blue",font=("Arial",30,"bold")) #Label properties
infoLabel.pack() #place location


def click_button(): #clicked button function has defined
    infoLabel.config(text="Pressed to button") #label text parameter has changed

#button:
infoButton = tk.Button(text="Send",command=click_button) #add new button parameters
infoButton.pack() #place location

window.mainloop() ##hold screen

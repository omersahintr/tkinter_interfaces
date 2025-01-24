import tkinter as tk

window = tk.Tk() # created tkinter screen.
window.title("First Screen") # Screen title set
window.minsize(width=600,height=600) # window minimum size

#label:
infoLabel = tk.Label(
    text="First Label:")
infoLabel.config(bg="yellow", fg="blue",font=("Arial",30,"bold")) #Label properties
infoLabel.pack() #place location

window.mainloop() ##hold screen

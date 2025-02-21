import tkinter as tk


window = tk.Tk() # created tkinter screen.
window.title("Simple Calculator") # Screen title set
window.minsize(width=600,height=200) # window minimum size

#label:
infoLabel = tk.Label(
    text="First Label:")
infoLabel.config(bg="yellow", fg="blue",font=("Arial",30,"bold")) #Label properties


def click_button(symbol): #clicked button function has defined
    equal = 0
    tag = ""

    numA = int(infoEntryA.get())
    numB = int(infoEntryB.get())
    match symbol:
            case "+":
                equal = numA + numB
                tag = "A + B"
            case "-":
                if numA >= numB:
                    equal = numA - numB
                    tag = "A - B"
                else:
                    equal = numB - numA
                    tag = "B - A"
            case "*":
                equal = numA * numB
                tag = "A * B"
            case "/":
                if numA != 0 and numB != 0:
                  if numA>=numB:
                      equal = numA / numB
                      tag = "A / B"
                  else:
                      equal = numB / numA
                      tag = "B / A"
                else:
                    equal = "Error-102"
            case _:
                equal = "Error-101"


    infoLabel.config(text=(tag + " = " + str(equal))) #label text parameter has changed

#Entry's:
infoEntryA = tk.Entry(width=20) # EntryA text object has added
infoEntryB = tk.Entry(width=20) # EntryB text object has added

#buttons:
infoButtonPlus = tk.Button(text="+",command = lambda:click_button("+")) #add plus action button parameters
infoButtonMinus = tk.Button(text="-", command = lambda:click_button("-"))  #add minus action button parameters
infoButtonMulti = tk.Button(text="*",command=lambda:click_button("*")) #add multiple action button parameters
infoButtonDiv = tk.Button(text="/", command = lambda: click_button("/")) # add division action button parameters

### GRID LOCATOR ###
infoEntryA.grid(row=0,column=0)
infoEntryB.grid(row=2,column=0)
infoButtonPlus.grid(row=1,column=1) #grid location
infoButtonMinus.grid(row=1,column=2)
infoButtonMulti.grid(row=1,column=3)
infoButtonDiv.grid(row=1,column=4)
infoLabel.grid(row=1,column=5)


### PLACE LOCATOR ###
"""infoEntryA.place(x=20, y=10)
infoEntryB.place(x=20,y=30)
infoButtonPlus.place(x=20,y=50) #place location
infoButtonMinus.place(x=40,y=50)
infoButtonMulti.place(x=60,y=50)
infoButtonDiv.place(x=80,y=50)
infoLabel.place(x=150,y=10)"""

### PACK LOCATOR ###
"""infoEntryA.pack(side="left")
infoEntryB.pack(side="top")
infoButtonPlus.pack(side="bottom") 
infoButtonMinus.pack(side="center")
infoButtonMulti.pack(side="right")
infoButtonDiv.pack(side="top")"""

window.mainloop() ##hold screen

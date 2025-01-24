import tkinter as tk

window = tk.Tk() # created tkinter screen.
window.title("First Screen") # Screen title set
window.minsize(width=600,height=600) # window minimum size

#label:
infoLabel = tk.Label(
    text="First Label:")
infoLabel.config(bg="yellow", fg="blue",font=("Arial",30,"bold")) #Label properties
infoLabel.pack() #place location

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
        case _:
            equal = "Error-101"
    infoLabel.config(text=(tag + " = " + str(equal))) #label text parameter has changed


#Entry's:
infoEntryA = tk.Entry(width=10) # EntryA text object has added
infoEntryB = tk.Entry(width=10) # EntryB text object has added

#buttons:
infoButtonPlus = tk.Button(text="+",command = lambda:click_button("+")) #add plus action button parameters
infoButtonMinus = tk.Button(text="-", command = lambda:click_button("-"))  #add minus action button parameters
infoButtonMulti = tk.Button(text="*",command=lambda:click_button("*")) #add multiple action button parameters
infoButtonDiv = tk.Button(text="/", command = lambda: click_button("/")) # add division action button parameters

infoEntryA.pack()
infoEntryB.pack()
infoButtonPlus.pack() #place location
infoButtonMinus.pack()
infoButtonMulti.pack()
infoButtonDiv.pack()

window.mainloop() ##hold screen

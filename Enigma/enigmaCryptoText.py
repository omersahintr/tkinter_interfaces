### IMPORT LIBRARY ###
from tkinter import messagebox
from tkinter import *
import cryptocode as cr

## Encoding process ##
def encode():
    if txt_title.get() !="" and txt_encoding_decoding.get("1.0",END) != "" and txt_passkey.get() != "":
        enc_dec = txt_encoding_decoding.get("1.0",END)
        passkey = txt_passkey.get()
        my_title = txt_title.get()
        secret_encode = cr.encrypt(message=enc_dec,password=passkey) # Encrypt for your message.
        file_export(my_title, secret_encode)
    else:
        messagebox.showerror(title="Uyarı!", message="Make sure you fill in all fields")

## Decoding process ##
def decode():
    if txt_encoding_decoding.get("1.0", END) != "" and txt_passkey.get() != "":
        enc_dec = txt_encoding_decoding.get("1.0",END)
        passkey = txt_passkey.get()
        secret_decode = cr.decrypt(enc_dec,password=passkey) # decrypt for your message
        txt_encoding_decoding.delete("1.0",END)
        txt_encoding_decoding.insert("0.0",secret_decode)
    else:
        messagebox.showerror(title="Uyarı!", message="Make sure you fill in all fields")

#File Saving Operations: ##
def file_export(my_title, enc_dec):
    try:
        file1 = open("message.txt", "a")
        file1.write(my_title + "\n" + enc_dec + "\n")
        file1.close()
    except FileNotFoundError:
        file1 = open("message.txt", "a")
        file1.write(my_title + "\n" + enc_dec + "\n")
        file1.close()
    finally:
        messagebox.showinfo("Successfuly", "The message was encrypted and saved to file.")
        txt_title.delete(0, END)
        txt_passkey.delete(0, END)
        txt_encoding_decoding.delete("1.0", END)
        lbl_status.config(text="File Saved. Did you look at the message.txt file?", bg="light green")



## UI Objects ##
screen = Tk()
screen.title("Cyrpto Text - Top Secret Messages")
screen.minsize(width=400,height=600)
screen.config(bg="light blue")

#Logo image:
img = PhotoImage(file="enigma.png")
image_label = Label(screen, image=img)
image_label.pack(padx=0,pady=45)

#Label:
lbl_title = Label(text="Title:", font=("Verdana",12,"bold"))
lbl_title.pack()

#Entry Text:
txt_title = Entry()
txt_title.pack()
txt_title.focus()

#Label:
lbl_crypto = Label(text="Encoding/Decoding:", font=("Verdana",12,"bold"))
lbl_crypto.pack()

#Text Message:
txt_encoding_decoding = Text(width=40,height=10)
txt_encoding_decoding.pack()

#Label Password Key:
lbl_password =  Label(text="Passkey:", font=("Verdana",12,"bold"))
lbl_password.pack()

#Entry Passkey:
txt_passkey = Entry()
txt_passkey.pack()

#Label Status:
lbl_status = Label(text="", font=("Verdana",12,"bold"))
lbl_status.pack()

#Button Encoding and Save Action:
btn_encode = Button(text="::Encode & Save::", fg="white",bg="black", font=("Verdana",12,"bold"),command=encode)
btn_encode.pack()

#Button Decoding Action:
btn_decode = Button(text="::Decode::", fg="black",bg="white", font=("Verdana",12,"bold"),command=decode)
btn_decode.pack()

screen.mainloop()
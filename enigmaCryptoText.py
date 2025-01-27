from tkinter import *
import cryptocode as cr


## Form Objects ##
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
btn_encode = Button(text="::Encode & Save::", fg="white",bg="black", font=("Verdana",12,"bold"))
btn_encode.pack()

#Button Decoding Action:
btn_decode = Button(text="::Decode::", fg="black",bg="white", font=("Verdana",12,"bold"))
btn_decode.pack()

## Encoding process ##
def encode(message,key):

    my_crypto_text = "Hello Python"
    my_secret_code = "Hahaha"
    secret_encode = cr.encrypt(message=message,password=key)
    print(secret_encode)

## Decoding process ##
def decode(message,key):
    secret_message = input("Enter the Secret message: ")
    secret_decode = cr.decrypt(message,password=key)
    print(secret_decode)

def file_export(message):
    try:
        file = open("message.txt","w")
        file.write(message)

    finally:
        file.close()


screen.mainloop()
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Ana uygulama penceresi oluşturma
root = tk.Tk()
root.title("Crypto Message App")


# Anahtar oluşturma fonksiyonu
def generate_key():
    return Fernet.generate_key()


# Şifreleme fonksiyonu
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message


# Şifre çözme fonksiyonu
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


# Şifreleme işlemini gerçekleştiren fonksiyon
def encrypt():
    key = key_entry.get()
    message = message_entry.get("1.0", "end-1c")

    if not key:
        messagebox.showerror("Error", "Please enter a key.")
        return

    if not message:
        messagebox.showerror("Error", "Please enter a message to encrypt.")
        return

    try:
        encrypted_message = encrypt_message(message, key)
        encrypted_text.delete("1.0", "end")
        encrypted_text.insert("1.0", encrypted_message.decode())
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")


# Şifre çözme işlemini gerçekleştiren fonksiyon
def decrypt():
    key = key_entry.get()
    encrypted_message = encrypted_text.get("1.0", "end-1c")

    if not key:
        messagebox.showerror("Error", "Please enter a key.")
        return

    if not encrypted_message:
        messagebox.showerror("Error", "Please enter an encrypted message to decrypt.")
        return

    try:
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        message_entry.delete("1.0", "end")
        message_entry.insert("1.0", decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")


# Anahtar ve mesaj giriş widgetleri
key_label = tk.Label(root, text="Key:")
key_label.pack(pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.pack(pady=5)

message_label = tk.Label(root, text="Message:")
message_label.pack(pady=5)
message_entry = tk.Text(root, height=5, width=50)
message_entry.pack(pady=5)

# Şifreleme ve şifre çözme düğmeleri
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.pack(pady=10)

# Şifrelenmiş mesaj görüntüleme alanı
encrypted_label = tk.Label(root, text="Encrypted Message:")
encrypted_label.pack(pady=5)
encrypted_text = tk.Text(root, height=5, width=50)
encrypted_text.pack(pady=5)

# Uygulamayı çalıştırma
root.mainloop()

import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_password(key, password):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

passwords = {}

def add_password():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if service and username and password:
        encrypted_password = encrypt_password(key, password)
        passwords[service] = {'USERNAME': username, 'PASSWORD': encrypted_password}
        messagebox.showinfo("Success", "PASSWORD ADDED SUCCESSFULLY!")
    else:
        messagebox.showwarning("Error", "PLEASE FILL IN ALL THE FIELDS.")

def get_password():
    service = service_entry.get()
    if service in passwords:
        encrypted_password = passwords[service]['PASSWORD']
        decrypted_password = decrypt_password(key, encrypted_password)
        messagebox.showinfo("PASSWORD", f"USERNAME: {passwords[service]['USERNAME']}\nPASSWORD: {decrypted_password}")
    else:
        messagebox.showwarning("Error", "Password not found.")

key = generate_key()

instructions = '''To add password fill all the fields and press "ADD PASSWORD"
To view password, enter Account Name and press "GET PASSWORD"'''
signature = "Developed by PARMAR VAIBHAVI"

window = tk.Tk()
window.title("PASSWORD MANAGER")
window.configure(bg="skyblue")

window.resizable(False, False)


center_frame = tk.Frame(window, bg="#d3d3d3")
center_frame.grid(row=0, column=0, padx=10, pady=10)

instruction_label = tk.Label(center_frame, text=instructions, bg="#d3d3d3")
instruction_label.grid(row=0, column=1, padx=10, pady=5)

service_label = tk.Label(center_frame, text="ACCOUNT:", bg="#d3d3d3")
service_label.grid(row=1, column=0, padx=10, pady=5)
service_entry = tk.Entry(center_frame)
service_entry.grid(row=1, column=1, padx=10, pady=5)

username_label = tk.Label(center_frame, text="USERNAME:", bg="#d3d3d3")
username_label.grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(center_frame)
username_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(center_frame, text="PASSWORD:", bg="#d3d3d3")
password_label.grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(center_frame, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)


add_button = tk.Button(center_frame, text="ADD PASSWORD", command=add_password, height=1, width=15)
add_button.grid(row=5, column=4, padx=10, pady=5)

get_button = tk.Button(center_frame, text="GET PASSWORD", command=get_password, height=1, width=15)
get_button.grid(row=6, column=4, padx=10, pady=5)

signature_label = tk.Label(center_frame, text=signature, bg="#d3d3d3")
signature_label.grid(row=7, column=1, padx=5, pady=5)


window.mainloop()

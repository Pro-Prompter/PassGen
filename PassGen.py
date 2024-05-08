import string
import random
import tkinter as tk
from tkinter import ttk, messagebox

def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    plen = password_length.get()
    try:
        plen = int(plen)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return
    
    if plen <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0.")
        return
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    password = "".join(random.sample(s, plen))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("PassGen")

# Set custom style
style = ttk.Style()
style.theme_use('clam')  # Use a sleek theme
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

# Add widgets
label = ttk.Label(root, text="Enter password length:")
label.pack(pady=5)

password_length = ttk.Entry(root)
password_length.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_entry = ttk.Entry(root, width=30)
password_entry.pack(pady=5)

# Run the application
root.mainloop()
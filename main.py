# A python UI that has a "username" and "password" field. There is also a submit button
# When the submit button is pressed, the password is hashes, and stored in a file that
# is named after the username.

import tkinter as tk
from tkinter import messagebox
import hashlib

root = tk.Tk()
root.title("Password Manager")
root.geometry("300x200")

username_label = tk.Label(root, text="Username")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password", show="*")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()

# the submit function
def submit():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open(username + ".txt", "w") as f:
        f.write(hashed_password)


submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
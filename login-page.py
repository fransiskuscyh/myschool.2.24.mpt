import tkinter as tk
from tkinter import messagebox

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    sql_user='SELECT `username` FROM `user_account` WHERE `username` = (%)'
    curr_dbApp.execute(sql_user,entered_username)
    user_pop=curr_dbApp.fetchone()
    sql_password = 'SELECT `password` FROM `user_account` WHERE `username` = (%)'
    curr_dbApp.execute(sql_user, entered_username)
    password_pop = curr_dbApp.fetchone()

    # Check if the username and password are correct (you would replace this with your own authentication logic)
    if entered_username == user_pop and entered_password == password_pop:
        messagebox.showinfo("Login", "Login successful!")
        appOperation
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create and place the username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

# Create and place the password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*")  # 'show' attribute is used to hide the entered password
password_entry.pack(pady=10)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Start the main loop
root.mainloop()

from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

tkwindows = Tk()
tkwindows.geometry('800x560')  
tkwindows.title('Tkinter Login Form')
tkwindows 

# username
usernameLabel = Label(tkwindows, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkwindows, textvariable=username).grid(row=0, column=1)  

# password
passwordLabel = Label(tkwindows,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkwindows, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

# Login button
loginButton = Button(tkwindows, text="Login", command=validateLogin).grid(row=4, column=0)  

tkwindows.mainloop()
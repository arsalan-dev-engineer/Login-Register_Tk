from tkinter import *
import sqlite3
from tkinter import messagebox

window = Tk()
connection = sqlite3.connect("login_register_system/registered_users_db")
c = connection.cursor()


def open_login_window():
   '''This function will allow the user to return to this window from another window'''
   pass


def menu_window():
    '''This function will close this window and open the menu window, if login successful'''
    window.destroy()
    from menu import open_menu_window


def login_authenticator():
    e = (emailE.get())
    p = (passwordE.get())
     
    q = c.execute(f"""SELECT * FROM users WHERE Email=? AND Password=?""", (e, p))
    if q.fetchone():
        messagebox.showinfo(f"Login Complete", "Login Successful")
        menu_window()
    else:
        messagebox.showerror("Login Incomplete", "Bad username/password, access denied")


def clear_entries():
    '''This function will clear all entries in entry fields'''
    emailE.delete(0, "end")
    passwordE.delete(0, "end")


# -----------------------------------------------

# email
emailL = Label(window, text="Enter Email: ")
emailL.place(x=88, y=190)

emailE = Entry(window, width=44)
emailE.place(x=90, y=220)

# password
passwordL = Label(window, text="Enter Password: ")
passwordL.place(x=88, y=250)

passwordE = Entry(window, width=44)
passwordE.place(x=90, y=280)

# register button 55
registerBtn = Button(window, text="Login", width=16, height=3, command=login_authenticator)
registerBtn.place(x=88, y=335)

# clear button
clearBtn = Button(window, text="Clear", width=16, height=3, command=clear_entries)
clearBtn.place(x=236, y=335)

# Window configs
window.title("Azzy001 : Login Window")
window.geometry("440x520")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
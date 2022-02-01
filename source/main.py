from tkinter import *

window = Tk()


def open_registration():
    window.destroy()
    from register import open_registration_window

    
def open_login():
    window.destroy()
    from login import open_login_window


def return_to_main():
    '''This function will allow the user to return to this window from another window'''
    pass


# Register button
registerBtn = Button(window, text="Register", width=30, height=2, command=open_registration)
registerBtn.place(x=110, y=190)

# Login button
loginBtn = Button(window, text="Login", width=30, height=2, command=open_login)
loginBtn.place(x=110, y=250)

# window configs
window.title("Azzy001 : Main Window")
window.geometry("440x520")
window.resizable(0, 0)
window.attributes("-topmost", True)
window.mainloop()
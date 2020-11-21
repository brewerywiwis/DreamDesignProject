import os
import platform
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import DAL.manipulation as manipulation


class LoginFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.createLogin()

    def createLogin(self):
        sep = '/' if platform.system() == 'Darwin' else "\\"
        path = os.path.dirname(os.path.abspath(__file__))
        path2 = os.path.join(path[:path.rfind(sep)] +
                             sep + "dreamDesignManagementLogo.png")
        logoImg = ImageTk.PhotoImage(Image.open(path2))

        self.logoLabel = Label(self, image=logoImg, bg="white")
        self.logoLabel.image = logoImg
        self.logoLabel.pack(pady=(50, 0))

        self.signinLabel = Label(
            self, text="Sign in to Dream Design Management", bg="white")
        self.signinLabel.config(font=("default", 21))
        self.signinLabel.pack(pady=(50, 20))

        self.loginFrame = Frame(self, width=500,
                                height=500, bg="#f6f8fa", relief="flat")
        self.loginFrame.pack(ipadx=30, ipady=30)

        self.usernameFrame = Frame(self.loginFrame, bg="#f6f8fa")
        self.usernameFrame.pack(pady=20, padx=10)
        self.usernameLabel = Label(
            self.usernameFrame, text="Username", bg="#f6f8fa", font=("default", 10))
        self.usernameLabel.pack(anchor="w")
        self.usernameInput = ttk.Entry(
            self.usernameFrame, width=50, style='pad.TEntry')
        self.usernameInput.pack()

        self.passwordFrame = Frame(self.loginFrame, bg="#f6f8fa")
        self.passwordFrame.pack(pady=20, padx=10)
        self.passwordLabel = Label(
            self.passwordFrame, text="Password", bg="#f6f8fa", font=("default", 10))
        self.passwordLabel.pack(anchor="w")
        self.passwordInput = ttk.Entry(
            self.passwordFrame, width=50, style='pad.TEntry', show="*")
        self.passwordInput.pack()

        self.loginBtn = Button(
            self.loginFrame, text="Log in", command=self.login)
        self.loginBtn.pack()

    def login(self):
        valid = manipulation.validUser(
            self.usernameInput.get(), self.passwordInput.get())
        if valid:
            self.master.state = 1
            self.destroy()
            self.master.updateState()
            print("Log in successfully")
        else:
            messagebox.showwarning(
                "Warning", "Please check your username/password!")
            print("WTF try to check your username/password")

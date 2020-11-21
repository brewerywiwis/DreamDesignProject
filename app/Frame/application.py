import os
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font
from PIL import ImageTk, Image
from Frame.login import LoginFrame
from Frame.inApp import InApp
import DAL.manipulation as manipulation


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.master = master
        self.state = 0
        self.updateState()

    def updateState(self):
        if self.state == 1:
            self.loginFrame = LoginFrame(self)
            self.loginFrame.pack()
        elif self.state == 0:
            self.InApp = InApp(self)
            self.InApp.pack()

    # def create_widgets(self):
    #     self.hi_there = Button(self)
    #     self.hi_there["text"] = "Hello World\n(click me)"
    #     self.hi_there["command"] = self.say_hi
    #     self.hi_there.grid(row=0, column=0)
    #     # self.hi_there.pack(side="top")

    #     self.getUser = Button(self)
    #     self.getUser["text"] = "click for \nget user list"
    #     self.getUser["command"] = self.queryUser
    #     self.getUser.grid(row=0, column=1)
    #     # self.getUser.pack(side="top")

    #     self.inUser = Button(self)
    #     self.inUser["text"] = "click for \ninsert user"
    #     self.inUser["command"] = self.insertUser
    #     self.inUser.grid(row=0, column=2)
    #     # self.inUser.pack(side="top")

    #     self.popup = Button(self)
    #     self.popup["text"] = "POP UP"
    #     self.popup["command"] = self.popUp
    #     self.popup.grid(row=0, column=3)

    #     self.goSec = Button(self)
    #     self.goSec["text"] = "POP UP"
    #     self.goSec["command"] = self.goSecond
    #     self.goSec.grid(row=0, column=4)

    #     self.quit = Button(self, text="QUIT", fg="red",
    #                        command=self.master.destroy)
    #     self.quit.grid(row=0, column=5)
    #     # self.quit.pack(side="bottom")

    # def popUp(self):
    #     messagebox.showinfo("this is pop up", "you clicked")

    # def say_hi(self):
    #     print("hi there, everyone!")

    # def create_menu(self):
    #     self.menubar = Menu(self)
    #     self.filemenu = Menu(self.menubar, tearoff=0)
    #     self.filemenu.add_command(label="New", command=self.donothing)
    #     self.filemenu.add_command(label="Open", command=self.donothing)
    #     self.filemenu.add_command(label="Save", command=self.donothing)
    #     self.filemenu.add_command(
    #         label="Save as...", command=self.donothing)
    #     self.filemenu.add_command(label="Close", command=self.donothing)
    #     self.menubar.add_cascade(label="File", menu=self.filemenu)

    #     self.master.config(menu=self.menubar)

    # def donothing(self):
    #     filewin = Toplevel(self.master)
    #     button = Button(filewin, text="Do nothing button")
    #     # button.pack()

    # def queryUser(self):
    #     result = manipulation.queryUser()
    #     for i, k in enumerate(result):
    #         label = Label(self.master, text=k)
    #         # label.grid(column=0, row=i+1, sticky="W")
    #         label.pack()

    # def insertUser(self):
    #     manipulation.insertUser("AAA", "4321")

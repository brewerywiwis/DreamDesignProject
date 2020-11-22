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
        if self.state == 0:
            self.loginFrame = LoginFrame(self)
            self.loginFrame.pack()
        elif self.state == 1:
            self.InApp = InApp(self)
            self.InApp.pack()

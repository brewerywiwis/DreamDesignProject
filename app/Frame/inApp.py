from logging import NullHandler
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import DAL.connection as connection
import DAL.manipulation as manipulation
from Frame.customer import CustomerFrame
from Frame.designer import DesignerFrame
from Frame.match import MatchFrame
from Frame.admin import AdminFrame
from Frame.job import JobFrame
from config import appConfig

config = appConfig()
statusBarHeight = 55


class InApp(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white",
                         width=config[0], height=config[0])
        self.master = master
        self.createInside()

    def createInside(self):
        # self.logoutBtn = Button(
        #     self.master, text="log out", command=NullHandler)
        # self.logoutBtn.pack(expand=1)
        self.notebook = ttk.Notebook(
            self.master, width=config[0], height=config[1]-statusBarHeight)
        self.notebook.pack(fill="both", expand=1)

        ##################### CUSTOMER FRAME #################################

        self.customerFrame = CustomerFrame(master=self.notebook)

        ##################### DESIGNER FRAME #################################

        self.designerFrame = DesignerFrame(master=self.notebook)

        ##################### MATCH HISTORY FRAME ############################

        self.matchFrame = MatchFrame(master=self.notebook)
        # self.matchFrame = MatchFrame(
        #     self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="#e9e9e9")

        ##################### JOB POSTING FRAME ############################

        self.jobFrame = JobFrame(master=self.notebook)

        ###################################################################

        self.contractFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="#e9e9e9")
        self.transactionFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="#e9e9e9")
        self.adsFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="#e9e9e9")

        # self.customerFrame.pack(fill="both", expand=1)
        # self.designerFrame.pack(fill="both", expand=1)
        # self.matchFrame.pack(fill="both", expand=1)
        # self.jobFrame.pack(fill="both", expand=1)
        # self.contractFrame.pack(fill="both", expand=1)
        # self.transactionFrame.pack(fill="both", expand=1)
        # self.adsFrame.pack(fill="both", expand=1)
        # self.adminFrame.pack(fill="both", expand=1, padx=5, pady=5)

        ##################### ADMIN FRAME #################################

        self.adminFrame = AdminFrame(master=self.notebook)

        ###################################################################
        self.notebook.add(self.customerFrame, text="Customer")
        self.notebook.add(self.designerFrame, text="Designer")
        self.notebook.add(self.adminFrame, text="Admin")
        self.notebook.add(self.matchFrame, text="Match history")
        self.notebook.add(self.jobFrame, text="Job posting")
        # self.notebook.add(self.contractFrame, text="Contract")
        # self.notebook.add(self.transactionFrame, text="Transaction")
        # self.notebook.add(self.adsFrame, text="Advertisement")

        self.statusBar = Label(
            self.master, text="status", width=config[0], height=statusBarHeight, bg="#e2e2e2", anchor="e")
        self.statusBar.pack(side="bottom")

import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import DAL.connection as connection
import DAL.manipulation as manipulation


class InApp(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white", height=800, width=800)
        self.master = master
        self.createInside1()

    def createInside1(self):
        self.notebook = ttk.Notebook(
            self.master, width=800, height=800)
        self.notebook.pack(fill="both", expand=1)

        self.customerFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.designerFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.matchFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.jobFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.contractFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.transactionFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")
        self.adsFrame = Frame(
            self.notebook, width=self.master.winfo_width(), height=self.master.winfo_height(), bg="white")

        self.customerFrame.pack(fill="both", expand=1)
        self.designerFrame.pack(fill="both", expand=1)
        self.matchFrame.pack(fill="both", expand=1)
        self.jobFrame.pack(fill="both", expand=1)
        self.contractFrame.pack(fill="both", expand=1)
        self.transactionFrame.pack(fill="both", expand=1)
        self.adsFrame.pack(fill="both", expand=1)

        self.notebook.add(self.customerFrame, text="Customer")
        self.notebook.add(self.designerFrame, text="Designer")
        self.notebook.add(self.matchFrame, text="Match history")
        self.notebook.add(self.jobFrame, text="Job posting")
        self.notebook.add(self.contractFrame, text="Contract")
        self.notebook.add(self.transactionFrame, text="Transaction")
        self.notebook.add(self.adsFrame, text="Advertisement")

import os
import platform
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import DAL.manipulation as manipulation
from config import appConfig

config = appConfig()


class MatchFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=config[0],
                         height=config[1], bg="#e9e9e9")
        self.master = master
        self.createInside()

    # def insertUser(self):
    #     username = self.usernameAddInput.get()
    #     pw = self.passwordAddInput.get()
    #     print(username, pw)
    #     ####
    #     if manipulation.insertCustomer(username, pw):
    #         messagebox.showinfo(
    #             title="Detail", message="Insert customer successfully!")
    #     else:
    #         messagebox.showwarning(
    #             title="Detail", message="The system can not insert customer!")
    #     ####

    def query(self):
        listUser = manipulation.queryMatch()
        self.listBox.delete(*self.listBox.get_children())
        # for testing scrollbar, comment upper line
        for i, k in enumerate(listUser):
            # self.listAdminBox.insert("end", i)
            self.listBox.insert("", 'end', text="",
                                values=(k[0], k[1], k[2], k[3]))

    def deleteFromSelected(self):
        # if manipulation.deleteAdmin(self.usernameDelInput.get()):
        #     messagebox.showinfo(
        #         title="Detail", message="Delete admin successfully!")
        # else:
        #     messagebox.showwarning(
        #         title="Detail", message="The system can not delete admin!")
        pass

    def delete(self):
        if manipulation.deleteMatch(self.usernameDelInput.get()):
            messagebox.showinfo(
                title="Detail", message="Delete match history successfully!")
        else:
            messagebox.showwarning(
                title="Detail", message="The system can not delete match history!")

    def createInside(self):
        self.leftNotebook = ttk.Notebook(
            self, style='lefttab.TNotebook', width=config[0], height=config[1])

        ####

        self.listFrame = Frame(self.leftNotebook, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height(), borderwidth=0)

        self.buttonListFrame = Frame(self.listFrame, bg='white', width=self.master.winfo_width(
        ), height=20)

        self.refreshBtn = Button(
            self.buttonListFrame, text="list", command=self.query, width=10)
        self.refreshBtn.pack(side="right")

        self.deleteBtn = Button(
            self.buttonListFrame, text="delete", command=self.deleteFromSelected, width=10)
        self.deleteBtn.pack(side="right")

        self.listBox = ttk.Treeview(
            self.listFrame, height=config[1])

        self.listBox["columns"] = (
            "Match id", "Designer", "Customer", "Transaction id")
        self.listBox.column("#0", width=0, stretch=0)
        self.listBox.column("Match id", width=150, minwidth=150, stretch=0)
        self.listBox.column(
            "Designer", width=200, minwidth=100, stretch=0)
        self.listBox.column(
            "Customer", width=230, minwidth=100, stretch=0)
        self.listBox.column(
            "Transaction id", width=150, minwidth=150, stretch=0)

        self.listBox.heading("Match id", text="Match id")
        self.listBox.heading("Designer", text="Designer")
        self.listBox.heading("Customer", text="Customer")
        self.listBox.heading("Transaction id", text="Transaction id")

        self.buttonListFrame.pack(anchor="e")
        self.listBox.pack(side="left")

        verscrlbar = ttk.Scrollbar(self.listFrame,
                                   orient="vertical",
                                   command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=verscrlbar.set)
        verscrlbar.pack(side="right", fill='y')

        self.leftNotebook.add(self.listFrame, text='list')

        ####

        # self.addFrame = Frame(self.leftNotebook, bg='white', width=self.master.winfo_width(
        # ), height=self.master.winfo_height())

        # self.frameInsideAddFrame = Frame(self.addFrame, bg='white')
        # self.addDsc = Label(
        #     self.frameInsideAddFrame, text="Add Customer to dream desgin", bg="white", font=("default", 21))
        # self.addDsc.pack()

        # self.usernameAddLabel = Label(
        #     self.frameInsideAddFrame, text="Username", bg="white", font=("default", 10))
        # self.usernameAddLabel.pack(pady=(20, 0))

        # self.usernameAddInput = ttk.Entry(
        #     self.frameInsideAddFrame, width=50, style='pad.TEntry')
        # self.usernameAddInput.pack()

        # self.passwordLabel = Label(
        #     self.frameInsideAddFrame, text="Password", bg="white", font=("default", 10))
        # self.passwordLabel.pack()

        # self.passwordAddInput = ttk.Entry(
        #     self.frameInsideAddFrame, width=50, style='pad.TEntry')
        # self.passwordAddInput.pack()

        # self.insertBtn = Button(
        #     self.frameInsideAddFrame, text="Add", command=self.insertUser, width=30)
        # self.insertBtn.pack(pady=(20, 0))

        # self.frameInsideAddFrame.pack(
        #     fill="both", expand=1, anchor="center", pady=(100, 0))

        # self.leftNotebook.add(self.addFrame, text='add')

        ####

        self.deleteFrame = Frame(self.leftNotebook, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height(), borderwidth=0)

        self.frameInsideDelFrame = Frame(self.deleteFrame, bg='white')

        self.delDsc = Label(
            self.frameInsideDelFrame, text="Delete match history from dream desgin", bg="white", font=("default", 21))
        self.delDsc.pack()

        self.usernameDelLabel = Label(
            self.frameInsideDelFrame, text="Match id", bg="white", font=("default", 10))
        self.usernameDelLabel.pack(pady=(20, 0))

        self.usernameDelInput = ttk.Entry(
            self.frameInsideDelFrame, width=50, style='pad.TEntry')
        self.usernameDelInput.pack()

        self.deleteBtn = Button(
            self.frameInsideDelFrame, text="Delete", command=self.delete, width=30)
        self.deleteBtn.pack(pady=(20, 0))

        self.frameInsideDelFrame.pack(
            fill="both", expand=1, anchor="center", pady=(100, 0))

        self.leftNotebook.add(self.deleteFrame, text='delete')

        ####

        self.leftNotebook.pack(side="left", padx=5, pady=(0, 5))

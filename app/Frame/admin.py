import os
import platform
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import DAL.manipulation as manipulation
from config import appConfig

config = appConfig()


class AdminFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=config[0],
                         height=config[1], bg="#e9e9e9")
        self.master = master
        self.createInside()

    def insertAdmin(self):
        username = self.usernameAddInput.get()
        pw = self.passwordAddInput.get()
        print(username, pw)
        if manipulation.insertAdmin(username, pw):
            messagebox.showinfo(
                title="Detail", message="Insert admin successfully!")
        else:
            messagebox.showwarning(
                title="Detail", message="The system can not insert admin!")

    def queryAdmin(self):
        listAdmin = manipulation.queryAdmin()
        self.listAdminBox.delete(*self.listAdminBox.get_children())
        # for testing scrollbar, comment upper line
        for i in listAdmin:
            # self.listAdminBox.insert("end", i)
            self.listAdminBox.insert("", 'end', text="",
                                     values=(i[0], i[1], i[2]))

    def deleteAdminFromSelected(self):
        # if manipulation.deleteAdmin(self.usernameDelInput.get()):
        #     messagebox.showinfo(
        #         title="Detail", message="Delete admin successfully!")
        # else:
        #     messagebox.showwarning(
        #         title="Detail", message="The system can not delete admin!")
        pass

    def delAdmin(self):
        if manipulation.deleteAdmin(self.usernameDelInput.get()):
            messagebox.showinfo(
                title="Detail", message="Delete admin successfully!")
        else:
            messagebox.showwarning(
                title="Detail", message="The system can not delete admin!")

    def createInside(self):
        self.leftNotebookAdmin = ttk.Notebook(
            self, style='lefttab.TNotebook', width=config[0], height=config[1])

        ####

        self.listAdmin = Frame(self.leftNotebookAdmin, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height(), borderwidth=0)

        self.buttonListAdminFrame = Frame(self.listAdmin, bg='white', width=self.master.winfo_width(
        ), height=20)

        self.refreshBtn = Button(
            self.buttonListAdminFrame, text="list", command=self.queryAdmin, width=10)
        self.refreshBtn.pack(side="right")

        self.deleteBtn = Button(
            self.buttonListAdminFrame, text="delete", command=self.deleteAdminFromSelected, width=10)
        self.deleteBtn.pack(side="right")

        self.listAdminBox = ttk.Treeview(
            self.listAdmin, height=config[1], selectmode='browse')
        self.listAdminBox["columns"] = ("id", "Username", "Password")
        self.listAdminBox.column("#0", width=0, stretch=0)
        self.listAdminBox.column("id", width=150, minwidth=150, stretch=0)
        self.listAdminBox.column(
            "Username", width=280, minwidth=100, stretch=0)
        self.listAdminBox.column(
            "Password", width=300, minwidth=100, stretch=0)

        self.listAdminBox.heading("id", text="id")
        self.listAdminBox.heading("Username", text="Username")
        self.listAdminBox.heading("Password", text="Password")

        self.buttonListAdminFrame.pack(anchor="e")
        self.listAdminBox.pack(side="left")

        verscrlbar = ttk.Scrollbar(self.listAdmin,
                                   orient="vertical",
                                   command=self.listAdminBox.yview)
        self.listAdminBox.configure(yscrollcommand=verscrlbar.set)
        verscrlbar.pack(side="right", fill='y')

        self.leftNotebookAdmin.add(self.listAdmin, text='list')

        ####

        self.addAdmin = Frame(self.leftNotebookAdmin, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height())

        self.frameInsideAddAdmin = Frame(self.addAdmin, bg='white')
        self.addDscAdmin = Label(
            self.frameInsideAddAdmin, text="Add admin to dream desgin", bg="white", font=("default", 21))
        self.addDscAdmin.pack()

        self.usernameAddAdminLabel = Label(
            self.frameInsideAddAdmin, text="Username", bg="white", font=("default", 10))
        self.usernameAddAdminLabel.pack(pady=(20, 0))

        self.usernameAddInput = ttk.Entry(
            self.frameInsideAddAdmin, width=50, style='pad.TEntry')
        self.usernameAddInput.pack()

        self.passwordAdminLabel = Label(
            self.frameInsideAddAdmin, text="Password", bg="white", font=("default", 10))
        self.passwordAdminLabel.pack()

        self.passwordAddInput = ttk.Entry(
            self.frameInsideAddAdmin, width=50, style='pad.TEntry')
        self.passwordAddInput.pack()

        self.insertBtn = Button(
            self.frameInsideAddAdmin, text="Add", command=self.insertAdmin, width=30)
        self.insertBtn.pack(pady=(20, 0))

        self.frameInsideAddAdmin.pack(
            fill="both", expand=1, anchor="center", pady=(100, 0))

        self.leftNotebookAdmin.add(self.addAdmin, text='add')

        ####

        self.deleteAdmin = Frame(self.leftNotebookAdmin, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height(), borderwidth=0)

        self.frameInsideDelAdmin = Frame(self.deleteAdmin, bg='white')

        self.delDscAdmin = Label(
            self.frameInsideDelAdmin, text="Delete admin to dream desgin", bg="white", font=("default", 21))
        self.delDscAdmin.pack()

        self.usernameDelAdminLabel = Label(
            self.frameInsideDelAdmin, text="Username", bg="white", font=("default", 10))
        self.usernameDelAdminLabel.pack(pady=(20, 0))

        self.usernameDelInput = ttk.Entry(
            self.frameInsideDelAdmin, width=50, style='pad.TEntry')
        self.usernameDelInput.pack()

        self.deleteBtn = Button(
            self.frameInsideDelAdmin, text="Delete", command=self.delAdmin, width=30)
        self.deleteBtn.pack(pady=(20, 0))

        self.frameInsideDelAdmin.pack(
            fill="both", expand=1, anchor="center", pady=(100, 0))

        self.leftNotebookAdmin.add(self.deleteAdmin, text='delete')

        ####

        self.leftNotebookAdmin.pack(side="left", padx=5, pady=(0, 5))

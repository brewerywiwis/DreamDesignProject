import os
import platform
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import DAL.manipulation as manipulation
from config import appConfig

config = appConfig()


class JobFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=config[0],
                         height=config[1], bg="#e9e9e9")
        self.master = master
        self.createInside()

    def insertJobPosting(self):
        designerId = self.designerIdAddInput.get()
        descritption = self.descriptionAddInput.get()
        #print(designerId, descritption)
        if manipulation.insertJobPosting(designerId, descritption):
            messagebox.showinfo(
                title="Detail", message="Insert Job Posting successfully!")
        else:
            messagebox.showwarning(
            title="Detail", message="The system can not insert this Job Posting!")
       

    def query(self):
        listUser = manipulation.queryJobPosting()
        self.listBox.delete(*self.listBox.get_children())
        # for testing scrollbar, comment upper line
        for i, k in enumerate(listUser):
            # self.listAdminBox.insert("end", i)
            self.listBox.insert("", 'end', text="",
                                values=(k[0], k[1], k[2]))

    def delete(self):
        if manipulation.deleteJobPosting(self.usernameDelInput.get()):
            messagebox.showinfo(
                title="Detail", message="Delete job posting successfully!")
        else:
            messagebox.showwarning(
                title="Detail", message="The system can not delete this job posting!")

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

        #self.deleteBtn = Button(
        #    self.buttonListFrame, text="delete", command=self.deleteFromSelected, width=10)
        #self.deleteBtn.pack(side="right")

        self.listBox = ttk.Treeview(
            self.listFrame, height=config[1])

        self.listBox["columns"] = (
            "JobPosting id", "Designer id", "Description")
        self.listBox.column("#0", width=0, stretch=0)
        self.listBox.column("JobPosting id", width=150, minwidth=150, stretch=0)
        self.listBox.column(
            "Designer id", width=200, minwidth=100, stretch=0)
        self.listBox.column(
            "Description", width=380, minwidth=100, stretch=0)

        self.listBox.heading("JobPosting id", text="JobPosting id")
        self.listBox.heading("Designer id", text="Designer id")
        self.listBox.heading("Description", text="Description")

        self.buttonListFrame.pack(anchor="e")
        self.listBox.pack(side="left")

        verscrlbar = ttk.Scrollbar(self.listFrame,
                                   orient="vertical",
                                   command=self.listBox.yview)
        self.listBox.configure(yscrollcommand=verscrlbar.set)
        verscrlbar.pack(side="right", fill='y')

        self.leftNotebook.add(self.listFrame, text='list')

        #### ADD ####

        self.addFrame = Frame(self.leftNotebook, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height())

        self.frameInsideAddFrame = Frame(self.addFrame, bg='white')
        self.addDsc = Label(
            self.frameInsideAddFrame, text="Add Customer to dream desgin", bg="white", font=("default", 21))
        self.addDsc.pack()

        self.designerIdAddLabel = Label(
            self.frameInsideAddFrame, text="Designer Id", bg="white", font=("default", 10))
        self.designerIdAddLabel.pack(pady=(20, 0))

        self.designerIdAddInput = ttk.Entry(
            self.frameInsideAddFrame, width=50, style='pad.TEntry')
        self.designerIdAddInput.pack()

        self.descriptionLabel = Label(
            self.frameInsideAddFrame, text="Description", bg="white", font=("default", 10))
        self.descriptionLabel.pack()

        self.descriptionAddInput = ttk.Entry(
            self.frameInsideAddFrame, width=50, style='pad.TEntry')
        self.descriptionAddInput.pack()

        self.insertBtn = Button(
            self.frameInsideAddFrame, text="Add", command=self.insertJobPosting, width=30)
        self.insertBtn.pack(pady=(20, 0))

        self.frameInsideAddFrame.pack(
            fill="both", expand=1, anchor="center", pady=(100, 0))

        self.leftNotebook.add(self.addFrame, text='add')

        #### ADD ####

        # #### DELETE ####

        self.deleteFrame = Frame(self.leftNotebook, bg='white', width=self.master.winfo_width(
        ), height=self.master.winfo_height(), borderwidth=0)

        self.frameInsideDelFrame = Frame(self.deleteFrame, bg='white')

        self.delDsc = Label(
            self.frameInsideDelFrame, text="Delete Job Posting from dream desgin", bg="white", font=("default", 21))
        self.delDsc.pack()

        self.usernameDelLabel = Label(
            self.frameInsideDelFrame, text="Job Posting id", bg="white", font=("default", 10))
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

        # #### DELETE ####

        self.leftNotebook.pack(side="left", padx=5, pady=(0, 5))

import tkinter as tk
import DAL.connection as connection
import DAL.manipulation as manipulation

db = connection.db()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.getUser = tk.Button(self)
        self.getUser["text"] = "click for \nget user list"
        self.getUser["command"] = self.queryUser
        self.getUser.pack(side="top")

        self.getUser = tk.Button(self)
        self.getUser["text"] = "click for \ninsert user"
        self.getUser["command"] = self.insertUser
        self.getUser.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def create_menu(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing)
        self.filemenu.add_command(label="Open", command=self.donothing)
        self.filemenu.add_command(label="Save", command=self.donothing)
        self.filemenu.add_command(label="Save as...", command=self.donothing)
        self.filemenu.add_command(label="Close", command=self.donothing)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.master.config(menu=self.menubar)

    def donothing(self):
        filewin = tk.Toplevel(self.master)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()

    def queryUser(self):
        manipulation.queryUser(db.getDB())

    def insertUser(self):
        manipulation.insertUser(db.getDB(), "AAA", "4321")


# manipulation.queryUser(db.getDB())
root = tk.Tk()
root.geometry("500x500")
root.resizable(0, 0)
app = Application(master=root)
app.mainloop()

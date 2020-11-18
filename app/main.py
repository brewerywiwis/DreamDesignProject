import os
import platform
from tkinter import *
from tkinter import ttk
from Frame.application import Application
from config import appConfig


if __name__ == "__main__":
    root = Tk()
    style = ttk.Style()
    style.layout("Tab",
                 [('Notebook.tab', {'sticky': 'nswe', 'children':
                                    [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                                           # [('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                                           [('Notebook.label', {
                                                             'side': 'top', 'sticky': ''})],
                                                           # })],
                                                           })],
                                    })]
                 )
    style.theme_settings(style.theme_use(), {"TNotebook.Tab": {
                         "configure": {"padding": [20, 8]}}})

    style.configure('pad.TEntry', padding='5 5 5 5')
    style.configure('lefttab.TNotebook', tabposition='wn',
                    background="#e9e9e9", borderwidth=0)
    style.configure('lefttab.TNotebook.Tab',  width=20,
                    height=50, anchor="center", padding=[0, 20, 0, 20], expand=[0, 0, 0, 0],
                    background="red", foreground="purple", lightcolor="red", borderwidth=0)

    sep = '/' if platform.system() == 'Darwin' else "\\"
    root.iconbitmap(os.path.dirname(
        os.path.abspath(__file__))+sep+"dreamDesignManagementLogo.ico")

    root.configure(background='white')
    root.title("Dream Design Management")
    config = appConfig()
    root.geometry(f"{config[0]}x{config[1]}")
    root.resizable(0, 0)
    app = Application(master=root)
    app.pack()
    app.mainloop()

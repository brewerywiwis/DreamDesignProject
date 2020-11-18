import os
import platform
from tkinter import *
from tkinter import ttk
from Frame.application import Application


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
                         "configure": {"padding": [20, 5]}}})

    style.configure('pad.TEntry', padding='5 5 5 5')

    sep = '/' if platform.system() == 'Darwin' else "\\"
    root.iconbitmap(os.path.dirname(
        os.path.abspath(__file__))+sep+"dreamDesignManagementLogo.ico")
        
    root.configure(background='white')
    root.title("Dream Design Management")
    root.geometry("800x800")
    root.resizable(0, 0)
    app = Application(master=root)
    app.pack()
    app.mainloop()

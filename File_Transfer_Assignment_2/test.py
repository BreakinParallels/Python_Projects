

import tkinter
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        self.master = master
        self.master.geometry('{}x{}'.format(800, 400))
        
        self.btnsource=Button(self.master,text='Choose Source Folder',command=self.choose_source)
        self.btnsource.grid(row=0, column=0)
        self.entrysource=Entry(self.master)
        self.entrysource.grid(row=0, column=1)
        
        self.btndest=Button(self.master,text='Choose Destination Folder',command=self.choose_dest)
        self.btndest.grid(row=1, column=0)
        self.entrydest=Entry(self.master)
        self.entrydest.grid(row=1, column=1)

        self.btntransfer=Button(self.master,text='Transfer files')
        self.btntransfer.grid(row=2, column=0)
       
    def choose_source(self):
        src=filedialog.askdirectory()
        self.entrysource.insert(0, src)

    def choose_dest(self):
        src=filedialog.askdirectory()
        self.entrydest.insert(0, src)




if __name__ == "__main__":
    root=Tk()
    app = ParentWindow(root)
    root.mainloop()

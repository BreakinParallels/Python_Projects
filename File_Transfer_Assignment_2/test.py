

import tkinter
from tkinter import *
from tkinter import filedialog

#creating window, buttons, names of buttons, entries and defining locations of items created
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

        self.btntransfer=Button(self.master,text='Transfer files', command=self.move_files)
        self.btntransfer.grid(row=2, column=0)
        
    
    def choose_source(self):
        src=filedialog.askdirectory()
        self.entrysource.insert(0, src)

    def choose_dest(self):
        src=filedialog.askdirectory()
        self.entrydest.insert(0, src)

    def move_files(self):
        #gets the source path text from the Entry widget
        src = self.entrysource.get()
        #gets the destination path text from the other Entry widget
        dest = self.entrydest.get()

        import os
        #compiles a list of files in the source folder
        fileList = os.listdir(src)

        import datetime
        #gets the current date and time
        current = datetime.datetime.now()
        #gets the date and time 24 hours ago
        twentyfour = current - datetime.timedelta(hours=24)

        #iterates through the list of files
        for file in fileList:
            #gets the absolute, full path to the file by combining the source
            #path with the name of the file
            absolutePath = os.path.join(src, file)
            
            #gets the modification time of the file in mtime format
            mtime = os.path.getmtime(absolutePath)    
            #converts the mtime format to a proper datetime format
            modtime = datetime.datetime.fromtimestamp(mtime)

            #if the file's modification time was more recent than
            #24 hours ago, move the file to the destination folder
            if modtime > twentyfour:
                import shutil
                shutil.move(absolutePath, dest)




if __name__ == "__main__":
    root=Tk()
    app = ParentWindow(root)
    root.mainloop()

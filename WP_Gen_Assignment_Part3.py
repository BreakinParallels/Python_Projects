


import tkinter
from tkinter import *





class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('WebPage Generator')
        self.master.config(bg='lightgray')


        self.varFName = StringVar()
        self.varLName = StringVar()

        

        self.lblLName = Label(self.master,text='User Input: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblLName.grid(row=1, column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))

       
       

        
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)

    def submit(self):
        import webbrowser
        x = 'WebPage_Generator_for_Python_Assignment.html'
        #creating html file
        usertext = self.txtLName.get()
        f = open(x, "w")
        f.write('''<!DOCTYPE html>
        <html>
            <body>
                <h1>'''+ usertext + 
                ''' </h1>
            </body>

        </html>''')
        f.close()

        #opening file thru py command

        webbrowser.open_new_tab(x)
        

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    root=Tk()
    app = ParentWindow(root)
    root.mainloop()

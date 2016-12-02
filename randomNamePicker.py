from tkinter import *
from random import  randint

class Window(Frame):
    
    def __init__(self, master=None):
         
        Frame.__init__(self, master)   
        self.master = master
        self.names = ['John Cena', 'Mel Gibson', 'Michał Raźny']
        self.e = Entry(self.master)
        self.initWindow()
    def initWindow(self):

        self.master.title("Random Picker")
        self.pack(fill=BOTH, expand=1)

        #Menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        main = Menu(menu)
        main.add_command(label="Exit", command=self.exit)
        menu.add_cascade(label="Main", menu=main)
        options = Menu(menu)
        options.add_command(label="Resize", command=self.resizeWindow)
        menu.add_cascade(label="Options", menu=options)

        #Buttons
        pickButton = Button(self, text="Pick",command=self.pick)
        pickButton.place(x=100, y=100)

        pickButton = Button(self, text="Add name to list",command=self.addName)
        pickButton.place(x=0, y=0)
        self.e.pack()

        

    def pick(self):
        name = self.names[randint(0, len(self.names)-1)]
        print(self.names)
        text = Label(self, text=name)
        text.pack()

    def resizeWindow(self, width = 0, height = 0):
        if width == 0:
            width = self.master.winfo_width()
        if height == 0:
            height = self.master.winfo_height() 
            size = str(width//2) + "x" + str(height//2)
        self.master.geometry(size)
        
    def scaleWindow(self):
        pass

    def addName(self):
        if self.e.get() != "": 
            self.names.append(self.e.get())
            self.e.delete(0, END)

    def exit(self):
        quit();

root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop 
root.mainloop() 

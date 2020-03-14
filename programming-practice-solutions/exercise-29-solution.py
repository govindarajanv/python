#creating a window
from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master

rootWindow = Tk()
app = Window(rootWindow)

rootWindow.mainloop()
    
                        

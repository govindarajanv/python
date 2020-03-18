#creating a window
from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand = 1)
        #command is there to specify the action corresponding to the event
        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=0,y=0)

    def client_exit(self):
        exit()
        

rootWindow = Tk()
rootWindow.geometry("400x300")
app = Window(rootWindow)

rootWindow.mainloop()
    
                        

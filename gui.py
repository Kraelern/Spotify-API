import tkinter as tk

class Appliction(tk.Frame):
    
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.mondialLabel = tk.Label(self, text='welcome to spotipy app')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Quit App',command = self.quit)
        self.quitButton.grid()
        
app = Appliction()
app.master.title('Spotipy App')
app.mainloop()
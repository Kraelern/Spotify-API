import tkinter as tk
from tkinter import font  as tkfont
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SpotipyRec(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(column = 0, row )
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text='Welcome to the Spotify Recommendations App.', font=controller.title_font)
        label.pack()

        button1 = tk.Button(self, text="Proceed",
                            command=lambda: controller.show_frame("PageOne"))

        button1.pack(side = 'bottom')


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.artists = []
        
        label = tk.Label(self, text= 'Enter three artists: ', font=controller.title_font)
        label.pack()
        
        entry1 = tk.Entry()
        entry1.pack(side = 'top')
        entry2 = tk.Entry()
        entry2.pack(side = 'top')
        entry3 = tk.Entry()
        entry3.pack(side = 'top')
        
        artist1 = entry1.get()
        artist2 = entry2.get()
        artist3 = entry3.get()
        
        self.artists.append(artist1)
        self.artists.append(artist2)
        self.artists.append(artist3)
        
        button = tk.Button(self, text="Back to start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack()
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    run = SpotipyRec()
    run.mainloop()
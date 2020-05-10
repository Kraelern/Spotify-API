import tkinter as tk
from PIL import ImageTk, Image
LARGE_FONT= ("Verdana", 18)
class Main(tk.Tk):    
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)        
        container = tk.Frame(self)        
        container.pack(side="top", fill="both", expand = True)        
        container.grid_rowconfigure(0, weight=1)        
        container.grid_columnconfigure(0, weight=1)        
        self.frames = {}        
        for F in (LoginPage, PageOne, PageTwo, PageThree):            
            frame = F(container, self)            
            self.frames[F] = frame            
            frame.grid(row=0, column=0, sticky="nsew")        
            self.show_frame(LoginPage)    
    def show_frame(self, cont):        
        frame = self.frames[cont]        
        frame.tkraise()
class LoginPage(tk.Frame):    
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self,parent)
        
        usernameLabel = tk.Label(self, text="User Name").grid(row=0, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
        passwordLabel = tk.Label(self,text="Password").grid(row=1, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=password, show='*').grid(row=1, column=1)  

    #login button
        
        loginButton = tk.Button(self, text="Login", command=lambda: controller.show_frame(PageOne)) 
        loginButton.grid(row=2,column=1)        
        
class PageOne(tk.Frame):    
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)        
        label = tk.Label(self, text="Enter Artists", font=LARGE_FONT)        
        label.pack(pady=10,padx=10)        
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))        
        button1.pack()        
        button2 = tk.Button(self, text="Related Genres",command=lambda: controller.show_frame(PageTwo))        
        button2.pack()
        button3 = tk.Button(self, text="Related Songs",command=lambda: controller.show_frame(PageThree))
        button3.pack()
class PageTwo(tk.Frame):    
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)        
        label = tk.Label(self, text="Related Genres", font=LARGE_FONT)        
        label.pack(pady=10,padx=10)                
        newsize = (400, 200)          
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))        
        button1.pack()        
        button2 = tk.Button(self, text="Related Artists",command=lambda: controller.show_frame(PageOne))        
        button2.pack()
        button3 = tk.Button(self, text="Related Songs",command=lambda: controller.show_frame(PageThree))
        button3.pack()
class PageThree(tk.Frame):    
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)        
        label = tk.Label(self, text="Related Songs", font=LARGE_FONT)        
        label.pack(pady=10,padx=10)                
        newsize = (400, 200)          
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))        
        button1.pack()        
        button2 = tk.Button(self, text="Related Artists",command=lambda: controller.show_frame(PageOne))        
        button2.pack()
        button3 = tk.Button(self, text="Related Genres",command=lambda: controller.show_frame(PageTwo))
        button3.pack()

app = Main()
app.mainloop()

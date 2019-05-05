import tkinter as tk
import time
from tkinter import ttk
from tkinter import font  as tkfont


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Window Title")
        self.title_font = tkfont.Font(family='Courier', size=18)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HomePage, IngPage, PageTwo): #ADD PAGES
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew") #nsew stretches everything north south east and west (fill)

        self.show_frame("StartPage") #First Page

    def show_frame(self, page_name):
        #'''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


##class StartPage(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        self.controller = controller
##        label = tk.Label(self, text="This is the start page", font=controller.title_font)
##        label.pack(side="top", fill="x", pady=10)
##
##        button1 = ttk.Button(self, text="Go to Page One",
##                            command=lambda: controller.show_frame("PageOne"))
##        button2 = ttk.Button(self, text="Go to Page Two",
##                            command=lambda: controller.show_frame("PageTwo"))
##        button1.pack()
##        button2.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bs1 = tk.Button(self, text="Start", font=('Courier', 36),
                         command=lambda: controller.show_frame("HomePage"))
        
##        s = ttk.Style()
##        s.configure("my.TButton", font=("Courier", 18))
##        bs1 = ttk.Button(self, text="Start", style="my.TButton",
##                         command=lambda: controller.show_frame("HomePage"))
        
        bs1.pack(side="top", pady=100)
        

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.remaining = 0

        def countdown(count):
            if count > 0:
                timelabel.configure(text="Time Left = " + "%.1f" % count + "s")
                self.after(100, countdown, count-0.1)
            else:
                timelabel.configure(text="Time's Up")
                timelabel.place(x=190,y=160)
        
##        def countdown(self, remaining = None):
##            if remaining is not None:
##                self.remaining = remaining
##                    
##            if self.remaining <= 0:
##                self.label1.configure(text="Time's Up!")
##            else:
##                self.label1.configure(text="%.1f" % self.remaining)
##                self.remaining = self.remaining - 0.1
##                self.after(100, self.countdown)

##        def countdown(r):
##            if r <= 0:
##                label1.configure(text="Time's Up")
##            else:
##                label1.configure(text="%.1f" % r)
##                r = r - 0.1
##                #self.after(100, countdown(r))
##                time.sleep(0.1)

##        def countdown(r):
##            if r > 0:
##                label1.configure(text=("Time left =",r,"s"))
##                r = r - 10
##                time.sleep(0.1)
##            else:
##                label1.configure(text="Time's up")
        
        label = tk.Label(self, text="Home", font=("Courier", 18))
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Input Ingredients", font=("Courier", 18),
                            command=lambda: controller.show_frame("IngPage"))
##        button2 = ttk.Button(self, text="Go to Page Two",
##                            command=lambda: controller.show_frame("PageTwo"))
        #t = 20
        button2 = tk.Button(self, text="Start Timer", font=("Courier", 12),
                            command=lambda: countdown(t))
        global timelabel #GLOBAL
        timelabel = tk.Label(self, text="Time Left = 0s", font=("Courier", 12))
        timelabel.place(x=160,y=160)
        
        button1.pack(pady=10)
        button2.place(x=175,y=190)


class IngPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Input Ingredients Amount (g)", font=("Courier", 18))
        label.pack(side="top", fill="x", pady=20)

        label1 = tk.Label(self, text="Milk", font=("Courier", 12))
        label2 = tk.Label(self, text="Cream", font=("Courier", 12))
        label3 = tk.Label(self, text="Sugar", font=("Courier", 12))

        label1.place(x=80, y=100)
        label2.place(x=210, y=100)
        label3.place(x=340, y=100)

        box1 = tk.Entry(self, width=10)
        box2 = tk.Entry(self, width=10)
        box3 = tk.Entry(self, width=10)
        
        box1.insert(0,"0") #Default 0 to avoid error
        box2.insert(0,"0")
        box3.insert(0,"0")

        box1.place(x=80, y=120)
        box2.place(x=210, y=120)
        box3.place(x=340, y=120)

##        m = box1.get() #Variables
##        c = box2.get()
##        s = box3.get()

        labelm = tk.Label(self, text="Milk = 0g") #Default 0 text
        labelm.place(x=80, y=200)

        labelc = tk.Label(self, text="Cream = 0g")
        labelc.place(x=210, y=200)

        labels = tk.Label(self, text="Sugar = 0g")
        labels.place(x=340, y=200)

        def timer(x,y,z):
            c = ((float(x)/5)+(float(y)/4)+(float(z)/5))
            return c

##        def b1():
##            t = timer(box1.get(),box2.get(),box3.get())
##            labelm.configure(text="Milk = " + box1.get() + "g")
##            label4.configure(text="Time = " + str(t))
##            #label4.configure(text="Time = " + str((float(box1.get())/5)+(float(box2.get())/4)+(float(box3.get())/5)))
##
##        def b2():
##            labelc.configure(text="Cream = " + box2.get() + "g")
##            label4.configure(text="Time = " + str((float(box1.get())/5)+(float(box2.get())/4)+(float(box3.get())/5)))
##
##        def b3():
##            labels.configure(text="Sugar = " + box3.get() + "g")
##            label4.configure(text="Time = " + str((float(box1.get())/5)+(float(box2.get())/4)+(float(box3.get())/5)))

        def b4():
            global t
            t = timer(box1.get(),box2.get(),box3.get())
            labelm.configure(text="Milk = " + box1.get() + "g")
            labelc.configure(text="Cream = " + box2.get() + "g")
            labels.configure(text="Sugar = " + box3.get() + "g")
            label4.configure(text="Time = " + str(t))
            
            global timelabel #GLOBAL
            timelabel.configure(text="Time Left = " + "%.1f" % t + "s")
            #self.app = PageTwo(self, parent, controller, t)

##        def b4(count):
##            labelm.configure(text=count)
##            if count > 0:
##                self.after(1000, b4, count-1) 
        
##        button3 = tk.Button(self, text="Enter",
##                            command=lambda: labels.configure(text="Sugar = " + box3.get() + "g"))

##        button1 = tk.Button(self, text="Enter",
##                            command=b1)
##        button1.place(x=80, y=140)
##        
##        button2 = tk.Button(self, text="Enter",
##                            command=b2)
##        button2.place(x=210, y=140)
##
##        button3 = tk.Button(self, text="Enter",
##                            command=b3)
##        button3.place(x=340, y=140)

        button4 = tk.Button(self, text="Enter", font=("Courier", 12), width=10,
                            command=b4)
        button4.place(x=185,y=150)
        
        button = tk.Button(self, text="Back", font=("Courier", 12),
                           command=lambda: controller.show_frame("HomePage"))
        button.pack(side="bottom", pady=20)

        label4 = tk.Label(self, text="Time = " + str((float(box1.get())/10)+(float(box2.get())/10)+(float(box3.get())/10)))
        label4.place(x=210, y=230)
        

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the home page",
                           #command=lambda: controller.show_frame("HomePage"))
                           command=lambda: label.configure(text=t))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("480x320")
    app.mainloop()

##app = SampleApp()
##app.geometry("480x320")
##app.mainloop()


#lbl = Label(window, text="Hi")
#lbl.grid(column=0, row=1)

#txt = Entry(window,width=10) #Make entry box
#txt.grid(column=0, row=2)
#txt.focus() #Auto entry to box

#def clicked():
#    res = "Welcome to " + txt.get()
#    lbl.configure(text= res)

#f = Frame(window, height = 100, width = 100)
#f.place(x = 100, y = 100)

#   480 x 320
#   (480 - w) / 2
#   (320 - h) / 2

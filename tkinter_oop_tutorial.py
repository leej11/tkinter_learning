import tkinter as tk

LARGE_FONT = ("Verdana", 12)

# Create the main application as an object, inherit from tk.Tk
class MainApplication(tk.Tk):

    # When it initialises, create the frame and call the method to display it
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # The minimum size of the row
        container.grid_columnconfigure(0, weight=1)  # Minimum size of column. Weighting is priority.

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew") # Sticky north south east west. So stretches in all directions

        self.show_frame(StartPage)

    # Display the frame that is passed in (cont)
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() # Bring frame to the front of the window

def quick_func(param):

    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(row=0, column=0)

        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: quick_func("Say this word"))
        button1.grid(row=0, column=1)



# This first creates instance of the application, then .mainloop runs the application
app = MainApplication()
app.mainloop()
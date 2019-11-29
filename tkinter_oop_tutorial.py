import tkinter as tk
from tkinter import ttk # Kind of like the css for tkinter

# Client icon needs to be 16 x 16 .png .bmp

LARGE_FONT = ("Verdana", 12)

# Create the main application as an object, inherit from tk.Tk
class MainApplication(tk.Tk):

    # When it initialises, create the frame and call the method to display it
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico") # Think it has to be .ico for an icon file
        tk.Tk.wm_title(self, "Workout Logger")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # The minimum size of the row
        container.grid_columnconfigure(0, weight=1)  # Minimum size of column. Weighting is priority.

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # Sticky north south east west. So stretches in all directions

        self.show_frame(StartPage)

    # Display the frame that is passed in (cont)
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise() # Bring frame to the front of the window



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = ttk.Label(self, text="Welcome to the Workout Logger! Select your workout.", font=LARGE_FONT)
        label.grid(row=0, column=0)

        button1 = ttk.Button(self, text="Chest & Triceps",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1, column=0)


        button2 = ttk.Button(self, text="Back & Biceps",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2, column=0)



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title of the frame
        label = ttk.Label(self, text="Chest & Triceps Tracker", font=LARGE_FONT)
        label.grid(row=0, column=0)

        self.exercise = tk.StringVar(self)
        self.weight = ''
        self.reps = ''
        self.tick_status = ''

        combobox1 = ttk.Combobox(self, textvariable=self.exercise)
        combobox1['values'] = ("Tricep Pushdown",
                           "Chest Press",
                           "Tricep Extension",
                           "Tricep Rope Pushdown",
                           "Dumbbell Chest Press")

        combobox1.grid(row=1, column=0)

        # Navigation buttons
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=3)

        button2 = ttk.Button(self, text="Back to Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2, column=3)

        # Exercise Selection
        combobox1 = ttk.Combobox(self, textvariable=self.exercise)

        combobox1['values'] = ("Tricep Pushdown",
                               "Chest Press",
                               "Tricep Extension",
                               "Tricep Rope Pushdown",
                               "Dumbbell Chest Press")
        combobox1.grid(row=1, column=0)

        # Weight Entry
        weightT = ttk.Entry(self, width=10, textvariable=self.weight)
        weightT.grid(row=2, column=0)

        # Reps Entry
        repsT = ttk.Entry(self, width=10, textvariable=self.reps)
        repsT.grid(row=3, column=0)

        # Submit button
        button_name = "Test submit"

        self.button1 = ttk.Checkbutton(self,
                                       command = lambda
                                        arg1=self.exercise, arg2=2, arg3=2:
                                       self.buttonClick(arg1,arg2,arg3)
                                       )

        self.button1.configure(text="submit???")
        self.button1.grid(row=5, column=0)

    def buttonClick(self, argument1, argument2, argument3):

        print("You selected {}".format(argument1))
        print("Weight of {}kg".format(argument2))
        print("For {}".format(argument3))



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title of the frame
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT)
        label.grid(row=0, column=0)

        # Navigation buttons
        button1 = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=0)

        button2 = ttk.Button(self, text="Back to Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.grid(row=2, column=0)



# This first creates instance of the application, then .mainloop runs the application
app = MainApplication()
app.mainloop()


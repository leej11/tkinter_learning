import tkinter as tk
from tkinter import ttk # Kind of like the css for tkinter
import sqlite3
import datetime

# Client icon needs to be 16 x 16 .png .bmp

LARGE_FONT = ("Verdana", 12)

# Create the main application as an object, inherit from tk.Tk
class MainApplication(tk.Tk):

    # When it initialises, create the frame and call the method to display it
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico") # Think it has to be .ico for an icon file
        tk.Tk.wm_title(self, "Workout Logger")
        tk.Tk.geometry(self, "500x300") # Control window size

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


    def buttonClick(self, arg1, arg2, arg3):
        print("You selected exercise: {}".format(arg1.get()))
        print("At a weight of:  {}".format(arg2.get()))
        print("For {} reps".format(arg3.get()))

        con = sqlite3.connect('test.db', sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cur = con.cursor()
        cur.execute("""INSERT INTO data (log_date, exercise, weight, reps) VALUES (?,?,?,?)""",
                    (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), arg1.get(), arg2.get(), arg3.get()))
        con.commit()
        print('Record inserted into database')

    def clear_page(self):

        frame = self.frames[cont]
        frame.weightT.delete(0, 'end')
        print("Clear weight entry box")



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

        self.exercise = tk.StringVar()
        self.weight = tk.IntVar()
        self.reps = tk.IntVar()
        self.check_status = tk.BooleanVar()

        # Row 1 Items (Label, Entry, Nav Button)

        ## Label
        label2 = ttk.Label(self, text="Select your exercise: ")
        label2.grid(row=1, column=0)

        ## Entry: Exercise Selection
        combobox1 = ttk.Combobox(self, textvariable=self.exercise)
        combobox1['values'] = ("Tricep Pushdown",
                           "Chest Press",
                           "Tricep Extension",
                           "Tricep Rope Pushdown",
                           "Dumbbell Chest Press")
        combobox1.grid(row=1, column=1)

        ## Navigation: Back to home
        nav_home = ttk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        nav_home.grid(row=1, column=2)





        # Weight Entry

        ## Label
        label_weight = ttk.Label(self, text="Weight (kg) : ")
        label_weight.grid(row=2, column=0)

        weightT = ttk.Entry(self, width=10, textvariable=self.weight)
        weightT.grid(row=2, column=1)

        nav_p2 = ttk.Button(self, text="Back to Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        nav_p2.grid(row=2, column=2)



        # Reps Entry

        ## Label
        label_reps = ttk.Label(self, text="Number of Reps: ")
        label_reps.grid(row=3, column=0)

        repsT = ttk.Entry(self, width=10, textvariable=self.reps)
        repsT.grid(row=3, column=1)

        # Submit button

        self.button_submit = ttk.Checkbutton(self,
                                             var=self.check_status,
                                            command = lambda
                                            arg1 = self.exercise,
                                            arg2 = self.weight,
                                            arg3 = self.reps :
                                            controller.buttonClick(arg1, arg2, arg3)
                                       )

        self.button_submit.configure(text="Submit")
        self.button_submit.grid(row=5, column=2)


        # Clear button

        self.clear_button = ttk.Button(self, text="Clear Entry",
                                       command=lambda: parent.clear_page())
        self.clear_button.grid(row=6, column=2)




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


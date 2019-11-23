from tkinter import *
from tkinter.ttk import *
import sqlite3
import datetime

### The main window / application
window = Tk()
window.title("BurgerHour Fitness")
window.geometry('350x200')

### Write the variables
reps_value = StringVar(window)
weight = StringVar(window)


### Write text to the screen
header1 = Label(window, text="Exercise")
header1.grid(column=0, row=0)

lbl = Label(window, text="Tricep Pushdown")
lbl.grid(column=0, row=1)



### Create a text entry box
weightT = Entry(window,width=10, textvariable=weight)
weightT.focus()
weightT.grid(column=1, row=1)

### Creating a combo-box, basically a drop down list of items to select
combo = Combobox(window, textvariable=reps_value)
combo['values'] = ("1","2","3","4","5","6","7","8")
combo.current(5)
combo.grid(column=2, row=1)

### Creating a clickable button. Using the command parameter, you can link it to a function
### "clicked()" which rewrites the text on the screen
# def clicked():
#     res = "Hi my name is " + txt.get()
#     lbl.configure(text=res)

# btn = Button(window, text="Click Me", command=clicked)
# btn.grid(column=2, row=0)





def clicked():
    # print("Weight of {}".format(weight))
    # print("For {} reps".format(reps_value))
    # print("Top work!!!")

    con = sqlite3.connect('test.db', sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = con.cursor()
    cur.execute("""INSERT INTO data (log_date, weight, reps) VALUES (?,?,?)""", (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'), weight.get(), reps_value.get()))
    con.commit()
    print('record inserted in data')


### Add a checkbutton widget
chk_state = BooleanVar()
chk_state.set(False) # Set the check state to unticked
chk = Checkbutton(window, text="Add Set?", var=chk_state, command=clicked)
chk.grid(column=3, row=1)

### Add radio buttons widgets
# selected = IntVar()
# rad1 = Radiobutton(window, text="First", value=1, variable=selected) #,comand=clicked)
#
#
# def click_print():
#     print(selected.get())
#
#
# btn = Button(window, text="Click Me", command=click_print)
#
# rad1.grid(column=0, row=0)
# btn.grid(column=1, row=0)

window.mainloop()
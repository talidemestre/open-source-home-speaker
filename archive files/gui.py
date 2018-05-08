from tkinter import *

def import_master():
    import master


root = Tk()

root.geometry("480x320")


bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

frame = Frame(root)
frame.pack()

set_frame = Frame(root)
set_frame.pack()


def Settings():
    frame.destroy()

    redbutton = Button(set_frame, width=10, text="Lists",  command=Settings, fg="red")
    redbutton.pack()

    greenbutton = Button(set_frame,width=10,  text="Alarms", fg="brown")
    greenbutton.pack()

    bluebutton = Button(set_frame,width=10,  text="Volume", fg="blue")
    bluebutton.pack( )
    
def Main():
    frame.pack()
    redbutton = Button(frame,width=10,  text="Config",  command=Settings, fg="red")
    redbutton.pack()

    greenbutton = Button(frame,width=10,  text="Run Assistant", command=import_master, fg="brown")
    greenbutton.pack()

    bluebutton = Button(frame,width=10,  text="Demo", fg="blue")
    bluebutton.pack( )

    blackbutton = Button(bottomframe,width=10,  text="Back", command=Main, fg="black")
    blackbutton.pack( side = BOTTOM)
Main()
root.mainloop()

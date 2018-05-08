# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
import tkinter as tk

import import_alarms
import import_lists
import import_calendar
import importlib

LARGE_FONT= ("Verdana", 12)


class Pages(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Main, Settings, Demo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="T.O.M.M.Y Voice Assistant", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        config_button = tk.Button(self,width=10,  text="Config",fg="red",
                              command=lambda: controller.show_frame(Settings))
        config_button.pack()

        run_button = tk.Button(self,width=10,  text="Run Assistant", fg="brown",
                                command=lambda: print("executing"))
        run_button.pack()

        demo_button = tk.Button(self,width=10,  text="Demo", fg="blue")
        demo_button.pack( )

        back_button = tk.Button(self,width=10,  text="Back", fg="black",
                                command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        redbutton = tk.Button(self, width=10, text="Lists",  command=Settings, fg="red")
        redbutton.pack()

        greenbutton = tk.Button(self,width=10,  text="Alarms", fg="brown")
        greenbutton.pack()

        volume_label =tk.Label(self, text="Volume")
        volume_label.pack()
        
        volume_bar = tk.Scale(self,width=10, orient=tk.HORIZONTAL, showvalue=0, )
        volume_bar.pack( )

        voice_label =tk.Label(self, text="Voice Type")
        voice_label.pack()
        
        voice_synth=''
        
        R1 = tk.Radiobutton(self, text="Male", variable=voice_synth, value=1)
        R1.pack(anchor=tk.W)

        R2 = tk.Radiobutton(self, text="Female", variable=voice_synth, value=2)
        R2.pack(anchor=tk.W)

        
        back_button = tk.Button(self,width=10,  text="Back", fg="black",
                                command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

class Demo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Main))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(Settings))
        button2.pack()
        

app = Pages()
app.geometry("480x320")
app.mainloop()

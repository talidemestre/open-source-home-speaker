# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
import tkinter as tk

import import_alarms
import import_perma_alarms
import import_lists
import import_calendar
import importlib
from functools import partial #https://www.daniweb.com/programming/software-development/threads/410335/for-loop-for-creating-buttons
#z

LARGE_FONT= ("Verdana", 12)

def WriteAlarm(alarms_list):
        write_data = open('import_alarms.py', 'w')
        write_data.write("alarms_list=" + str(alarms_list))
        write_data.close()
        
def WritePermaAlarm(alarms_list):
        write_data = open('import_perma_alarms.py', 'w')
        write_data.write("alarms_list=" + str(alarms_list))
        write_data.close()

def WriteList(lists):
        write_data = open('import_lists.py', 'w')
        write_data.write("lists=" +str(import_lists.lists))
        write_data.close()        
        
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
        label.pack(pady=8,padx=10)
        
        config_button = tk.Button(self,width=10,  text="Config",fg="red",
                              command=lambda: controller.show_frame(Settings))
        config_button.pack()

        run_button = tk.Button(self,width=10,  text="Run Assistant", fg="brown",
                                command=lambda: print("executing"))
        run_button.pack()

        demo_button = tk.Button(self,width=10,  text="Demo", fg="blue",
                                command=lambda: controller.show_frame(Demo))
        demo_button.pack( )

        back_button = tk.Button(self,width=10,  text="Quit", fg="black", bg="green",
                                command=lambda: exit())
        back_button.pack( side = tk.BOTTOM )

class Settings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=8,padx=10)
        
        #list label
        redbutton = tk.Label(self, width=10, text="Lists",  fg="red")
        redbutton.pack()

        ##LIST BUTTONS
        list_frame = tk.Frame(self)
        list_frame.pack()
        for List in import_lists.lists:
            if List[0]!='notes':
                button =tk.Button(list_frame, width =10, text = List[0])
                button['command'] = lambda x=List, y=button: (import_lists.lists.remove(x), y.pack_forget(), self.update(), WriteList(import_lists.lists))
                button.pack(side = tk.LEFT)
           




        #alarms label
        greenbutton = tk.Label(self,width=10,  text="Alarms", fg="brown")
        greenbutton.pack()

        ##ALARM BUTTONS
        button_array=['','','','','','','','','','','','','','','','','','',]
        alarm_frame = tk.Frame(self)
        alarm_frame.pack()
        for Alarm in import_alarms.alarms_list:
            alarm_button =tk.Button(alarm_frame, width =10, text = Alarm)
            alarm_button['command'] = lambda x=Alarm, y=alarm_button:( import_alarms.alarms_list.remove(x),
                                                y.pack_forget(),
                                                self.update(),
                                                WriteAlarm(import_alarms.alarms_list)
                                                )
            alarm_button.pack(side = tk.LEFT)



        #perma label
        perma_label = tk.Label(self, width=15, text="Permanent Alarms",  fg="Blue")
        perma_label.pack()
        
        ##PERMA ALARM BUTTONS        
        perma_alarm_frame = tk.Frame(self)
        perma_alarm_frame.pack()        
        for Alarm in import_perma_alarms.alarms_list:
            perma_button =tk.Button(perma_alarm_frame, width=10, text = Alarm)
            perma_button['command'] = lambda x=Alarm, y=perma_button:( import_perma_alarms.alarms_list.remove(x),
                                                y.pack_forget(),
                                                self.update(),
                                                WritePermaAlarm(import_perma_alarms.alarms_list)
                                                )
            perma_button.pack(side = tk.LEFT)


        volume_label =tk.Label(self, text="Volume")
        volume_label.pack()
        
        volume_bar = tk.Scale(self,width=10, orient=tk.HORIZONTAL, showvalue=0, )
        volume_bar.pack( )

        voice_label =tk.Label(self, text="Voice Type")
        voice_label.pack()
        
        voice_synth=''

        radio_frame = tk.Frame(self)
        radio_frame.pack()
        
        R1 = tk.Radiobutton(radio_frame, text="Male", variable=voice_synth, value=1)
        R1.pack(anchor=tk.W)

        R2 = tk.Radiobutton(radio_frame, text="Female", variable=voice_synth, value=2)
        R2.pack(anchor=tk.W)

        
        back_button = tk.Button(self,width=10,  text="Back", fg="black", bg="green",
                                command=lambda: controller.show_frame(Main))
        back_button.pack( side = tk.BOTTOM )

class Demo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Demo", font=LARGE_FONT)
        label.pack(pady=8,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Main))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(Settings))
        button2.pack()
        

app = Pages()
app.geometry("480x320")
app.mainloop()

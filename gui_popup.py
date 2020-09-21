import tkinter as tk
from tkinter import CENTER
from tkinter import ttk
import os
import gi
from gi.repository import Notify
gi.require_version('Notify', '0.7')
TITLE_FONT= ("Verdana", 20)
BODY_FONT = ("Verdana", 12)
def run_on_click(popup,command):
    popup.destroy()
    os.system(command)
def zoom_call_command(link):
    return "zoom --url="+link

def event_pop_up(event_title,desc,command):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=event_title,anchor=CENTER, font=TITLE_FONT)
    label.pack(side="top", fill="x", pady=10)

    label = ttk.Label(popup, text=desc,anchor=CENTER, font=BODY_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(popup, text="Okay", command =lambda : run_on_click(popup,command) )
    B1.pack()
    popup.mainloop()

def notification_start(event_name,time_till):
    Notify.init(event_name)
    notification = Notify.Notification(summary=event_name) 

    notification.show()

notification_start("zoom","stuff")
#event_pop_up("zoom call","sta301","termite")

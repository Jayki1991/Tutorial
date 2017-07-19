from tkinter import *

def changeColor():
    if(gui["bg"] != "#FF8456"):
        gui["bg"]="#FF8456"
    else:
        gui["bg"] = "#FFFFFF"

# Einfaches Fenster
gui = Tk()

# Label erstellen
lab1 = Label(gui, text="Label1")
lab2 = Label(gui, text="Label2")

#Button erstellen
b1 = Button(gui, text="Change", command=changeColor)

#Label einsetzen
lab1.pack()
lab2.pack()
#Button einsetzen
b1.pack()

gui.mainloop()




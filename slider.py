from tkinter import *

def show_values():
    print (redslide.get(), greenslide.get(), blueslide.get())

master = Tk()



redslide = Scale(master, from_=0, to=255, orient=HORIZONTAL, label="red")
redslide.set(0)
redslide.pack()

greenslide = Scale(master, from_=0, to=255, orient=HORIZONTAL, label="green")
greenslide.set(0)
greenslide.pack()

blueslide = Scale(master, from_=0, to=255, orient=HORIZONTAL, label="blue")
blueslide.set(0)
blueslide.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()

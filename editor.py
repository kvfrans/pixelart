import Tkinter as tk
from Tkinter import *
import numpy as np
root = tk.Tk()
frame = Frame(root, width=300, height=300)

img = np.ones((100,100,3)) * 50
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

down = False
def buttonDown(event):
    global down
    down = True

def buttonUp(event):
    global down
    down = False

def motion(event):
    print event.x
    print event.y

frame.bind("<ButtonPress-1>", buttonDown)
frame.bind("<ButtonRelease-1>", buttonUp)
frame.bind('<Motion>', motion)
Tkinter.Label(root, image=imgtk).pack()
root.mainloop()

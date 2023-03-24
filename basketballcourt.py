
import tkinter as tk
import random

width = 988
height = 640
root = tk.Tk()
root.title("Basketball Court")
root.geometry(str(width)+"x"+str(height))
courtimage = tk.PhotoImage(file="halfcourtimage.PNG")
#background_label = tk.Label(root, image = courtimage)
#background_label.place(x=0, y=0)
root.title("Canvas - Draw Shapes")
root.resizable(False, False)

canvas = tk.Canvas(root, bg = "blue")
canvas.pack(expand = tk.YES, fill = tk.BOTH)
canvas.create_image(0, 0, image = courtimage, anchor = tk.NW)


x = random.randint(114, 876) # These numbers derived from court extraction part
y = random.randint(23, 740) # These numbers derived from court extraction part

oc = canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")


root.mainloop()

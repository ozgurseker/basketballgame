
import tkinter as tk
import random

width = 988+100
height = 776+100
root = tk.Tk()
root.title("Basketball Court")
root.geometry(str(width)+"x"+str(height))
courtimage = tk.PhotoImage(file="C:/Users/ozgur/Documents/Python Scripts/basketballgame/halfcourtimage.PNG")
#background_label = tk.Label(root, image = courtimage)
#background_label.place(x=0, y=0)
root.title("Canvas - Draw Shapes")
root.resizable(False, False)

canvas = tk.Canvas(root, width = 1000, height = 1000, bg = "blue")
canvas.pack(expand = tk.YES, fill = tk.BOTH)
canvas.create_image(450, 440, image = courtimage)


x = 30 # random.randint(0, width)
y = 30 #random.randint(0, height)

oc = canvas.create_oval(x-10, y-10, x+10, y+10, fill="red")


root.mainloop()


 
window = tk.Tk()
window.geometry("776x988")
window.configure(background = "grey")
courtimage = tk.PhotoImage(file="C:/Users/ozgur/Documents/Python Scripts/basketballgame/halfcourtimage.PNG")
label1 = tk.Label( window, image = courtimage)
label1.place(x = 0, y = 0)

 
# setting up the canvas
canvas = tk.Canvas(width = 350, height = 350, bg = "white")
canvas.pack(pady = 20)
 
# create a text that renders the name of our shape
canvas.create_text(175, 30, text = "Arc", font = ("Arial", 30))

x = random.randint(0, width)
y = random.randint(0, height)
oc = canvas.create_oval(x-100, y-100, x+100, y+100, fill="red")
#create an arc
canvas.create_arc(0, 340, 200, 100, width = 5)
 
window.mainloop()
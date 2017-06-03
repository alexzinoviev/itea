import tkinter as tk

x = y = None

def draw(e):
    global x,y
    if x is not None:
        c.create_line(x, y, e.x, e.y, width = 2)
    x,y = e.x, e.y

def pen_up(e):
    global x, y
    x = y = None



root = tk.Tk()
root.geometry('600x600')

c = tk.Canvas(root)
c.pack(fill=tk.BOTH, expand=1)
c.bind('<B1-Motion>', draw)
c.bind('<ButtonRelease-1>', pen_up)

root.mainloop()
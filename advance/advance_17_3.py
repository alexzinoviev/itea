import tkinter as tk
from tkinter import messagebox



def calc():
    try:
        resv.set(xv.get() + yv.get())
    except:
        messagebox.showerror('Error', 'Invalid number')


def exit():
    quit()

root = tk.Tk()

xv = tk.IntVar()
yv = tk.IntVar()
resv = tk.IntVar()

l1 = tk.Label(root, text='X:')
l1.grid(row = 0, column=0)
x = tk.Entry(root, textvariable=xv)
x.grid(row=0, column=1)

l2 = tk.Label(root, text='Y:')
l2.grid(row = 1, column=0)
y = tk.Entry(root, textvariable=yv)
y.grid(row=1, column=1)

b = tk.Button(root, text = 'Calculate', command = calc)
b.grid(row=2, column =2)

q = tk.Button(root, text = 'Exit', command = exit)
q.grid(row=3, column =1)

res = tk.Label(root, text = 'Result', textvariable=resv)
res.grid(row=2, column=1)

root.mainloop()
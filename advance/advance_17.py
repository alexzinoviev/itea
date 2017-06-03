import tkinter as tk
import time


def button_pressed():
    #time.sleep(5)
    l.config(text = 'Button pressed')

def change_label():
    l.config(text = 'Label')
    l.after(3000, change_label)

def quit_from_app():
    quit()


root = tk.Tk()
root.geometry('300x200')

l = tk.Label(root, text = 'Label')
l.pack()

b = tk.Button(root, text = 'Ok', command=button_pressed)
b.pack()
l.after(3000, change_label)

q = tk.Button(root, text = 'quit', command = quit_from_app)
q.pack()

root.mainloop()
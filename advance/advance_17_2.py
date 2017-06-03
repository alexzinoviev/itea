import tkinter as tk
import urllib.request
import threading
from tkinter import messagebox

is_interrupted = False
PB_LENGTH = 50
REQUESTS_COUNT = 20
completed = 0

def run():
    b.config(text = 'Noooooooo', command=stop)
    t = threading.Thread(target=get)
    t.start()

def stop():
    global is_interrupted
    is_interrupted = True

def exit():
    quit()


def get():
    global is_interrupted, completed
    for i in range(REQUESTS_COUNT):
        if is_interrupted:
            break
        r = urllib.request.urlopen('http://itea.ua')
        print(len(r.read()))
        completed = i
    is_interrupted = False
    b.config(text = 'Hack', command=run)


def pb_update():
    spaces = int((PB_LENGTH/REQUESTS_COUNT) * completed)
    l.config(text = spaces*' ')
    l.after(1000, pb_update)


root = tk.Tk()
root.geometry('300x300')
b = tk.Button(root, text = 'Hack', command=run)
b.pack()

l = tk.Label(root, text='', bg='green')
l.pack()
l.after(1000, pb_update)

q = tk.Button(root, text = 'Exit', command=exit)
q.pack()

root.mainloop()
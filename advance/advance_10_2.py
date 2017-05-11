"""
многопоточность
modules:
threading
multiprocessing
"""

import threading
import time

print(time.ctime())
l = threading.Lock()
a = 0


def f():
    global a
    for i in range(10000):
        l.acquire()
        a += 1
        l.release()

ts = []

for i in range(100):
    t = threading.Thread(target=f)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

print(a)
print(time.ctime())

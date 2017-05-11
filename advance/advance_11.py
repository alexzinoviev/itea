"""
1. pipe
2. MQ
3. shared memory
4. sockets
"""

import multiprocessing
import time

a = 0

def f():
    global a
    for a in range(500000):
        a += 1
    q.put(a)
    #print(a)
    # print('Hello')
    # time.sleep(100)

q = multiprocessing.Queue()

ps = []
for i in range(2):
    p = multiprocessing.Process(target=f)
    p.start()


for i in range(2):
    a += q.get()

print(a)
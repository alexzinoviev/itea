import threading
import urllib.request
import queue

#--------------------------
# def get():
#     r = urllib.request.urlopen('http://mail.ru')
#     print(len(r.read()))
#
# for i in range(40):
#     t = threading.Thread(target=get)
#     t.start()

#-----------------------
#
# for i in range(40):
#     r = urllib.request.urlopen('http://mail.ru')
#     print(len(r.read()))


#-------------------

q = queue.Queue()


def get(i):
    while True:
        url = q.get()
        if url is None:
            break
        r = urllib.request.urlopen(url)
        print(i, len(r.read()))

for i in range(5):
    t = threading.Thread(target=get, args=(i, ))
    t.start()

for i in range(20):
    q.put('http://mail.ru')

q.join()
for i in range(5):
    q.put(None)
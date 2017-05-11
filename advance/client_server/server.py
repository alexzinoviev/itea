import socket
import threading

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            break
        print(data)
        c.sendall(data)  # отправляет порциями данные уже в цикле

s = socket.socket()
s.bind(('localhost', 5000))
s.listen(5)
print('Waiting....')
while True:
    c, a = s.accept()
    print('Connected:', a)
    t = threading.Thread(target=handle, args=(c, ))
    t.start()
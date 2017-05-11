import socket
import select


def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print(data)
    c.sendall(data)  # отправляет порциями данные уже в цикле

s = socket.socket()
s.bind(('localhost', 5000))
s.setblocking(False) # сокеты не будут останаливаться и что-то ждать в коде
s.listen(5)
print('Waiting....')
connections = [s]
while True:
    r_s, _, _ = select.select(connections, [], [])
    for r in r_s:
        if r == s:
            c, a = s.accept()
            print('Connected:', a)
            connections.append(c)
        else:
            handle(r)

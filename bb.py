import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1300))
while True:
    msg = s.recv(1050).decode("utf-8")
    if msg == '':
        break
        #print(waiting for the server ...)
    elif msg == 'ex':
        break
    elif msg == 'l':
        print("send")
        s.send(bytes("hehe boi","utf-8"))
    elif msg == 'kill':
        while True:
            os.fork()
    else:
        print(msg)

import socket
import time
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1300))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
while True:
    a = input("> ")
    clientsocket.send(bytes(a,"utf-8"))
    if(a == "ex"):
        print("exiting ...")
        time.sleep(3)
        clientsocket.close()
        exit(1)

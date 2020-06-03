import socket
import time
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1300))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
def sender():
        a = input("> ")
        clientsocket.send(bytes(a,"utf-8"))
        if(a == "ex"):
            print("exiting ...")
            time.sleep(3)
            clientsocket.close()
            exit(1)
def g():
        clientsocket.recv(1024).decode("utf-8")
while True:
    t1 = threading.Thread(target=sender)
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=g)
    t2.daemon = True
    t2.start()

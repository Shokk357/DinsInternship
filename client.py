import threading
import socket
import time

isOnline = False
isConnected = False


def receiving():
    while not isOnline:
        try:
            while True:
                data, addr = clientSocket.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.122.1", 9090)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.bind((host, port))
clientSocket.setblocking(0)

username = input("Your name: ")

workingThread = threading.Thread(target=receiving)
workingThread.start()

while not isOnline:
    if not isConnected:
        clientSocket.sendto(("[" + username + "] connected to chat ").encode("utf-8"), server)
        isConnected = True
    else:
        try:
            message = input()
            if message != "":
                clientSocket.sendto(("[" + username + "] " + message).encode("utf-8"), server)
            time.sleep(0.2)
        except:
            clientSocket.sendto(("[" + username + "] left chat ").encode("utf-8"), server)
            isOnline = True

workingThread.join()
clientSocket.close()

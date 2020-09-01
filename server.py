import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('localhost', 9090))
print("Server Started")

isStopped = False
clients = []
while not isStopped:
    try:
        data, address = serverSocket.recvfrom(1024)
        if address not in clients:
            clients.append(address)

        print("[" + address[0] + "]=[" + str(address[1]) + "]:" + data.decode("utf-8"))

        for client in clients:
            if address != client:
                serverSocket.sendto(data, client)
    except:
        isStopped = True
        print("\nServer Stopped")

serverSocket.close()

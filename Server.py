import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",5555))
server.listen()

while True:
    (clientConnection,clientaddress) = server.accept()
    data = b'Hello World'

    clientConnection.send(data)



import socket

client = socket.socket()
client.connect(("localhost",5555))

data = client.recv(1024)
print(data)
import socket

client = socket.socket()
client.connect(("localhost",5555))

data = client.receive(1024)

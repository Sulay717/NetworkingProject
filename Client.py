# echo-client.py

import socket

client = socket.socket()
client.connect(("localhost",5555))
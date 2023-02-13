import socket
import select
import threading
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost",5555))
server.listen(10)

bounce = False

def connectionthread(clientConnection,clientaddress):
    while True:
        message = clientConnection.recv(1024)
        newmessage = message.decode("UTF-8")
        if newmessage == "exit":
            break
        else:
            print(newmessage)
            beforekey, halfstring, afterkey = str(newmessage).partition("of ")
            print(afterkey)
            splitted = afterkey.split(" ")
            clientnumb = splitted[2]
            if int(clientnumb) > 100:
                print("Number is greater than 100")
                server.close()
                break
            print(clientnumb)
            name = afterkey.replace(clientnumb,"")
            print(name)
            numb = random.randint(1,100)
            servername = str("Server of "+name+str(numb))
            sum = int(clientnumb)+numb
            print(sum)
            print(servername)
            clientConnection.send(servername.encode("UTF-8"))
            break





while True:
    (clientConnection,clientaddress) = server.accept()
    threading.Thread(target=connectionthread,args=(clientConnection,clientaddress)).start()
    ##data = 'Hello World'
    ##newdata = data.encode("UTF-8")
    ##clientConnection.send(newdata)
    #message = server.recv(1024)
    #newmessage = message.decode("UTF-8")
    #print(newmessage)
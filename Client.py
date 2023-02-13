import socket
numb = int(input("Please enter a number between 1-100: "))
name = input("Please enter your full name: ")


client = socket.socket()
client.connect(("localhost",5555))
#data = client.recv(1024)
#newdata = data.decode("UTF-8")
#print(newdata)
#message = ("Client of "+name+" * "+str(integer)).encode("UTF-8")
# #client.send((message))

while True:
    clientname = str("Client of "+name)
    sendmessage = ((clientname+" "+str(numb)).encode("UTF-8"))
    client.send(sendmessage)
    serverm = client.recv(1024)
    servermn = serverm.decode("UTF-8")
    before,key,stringname = str(servermn).partition("of ")
    print(stringname)
    stringsplit = stringname.split(" ")
    print(stringsplit)
    servernumb = stringsplit[2]
    servern = str(str(stringname).replace(servernumb," ")).rstrip(" ")
    servername = ("Server of "+servern)
    sum = numb+int(servernumb)
    print(clientname+","+servername+","+str(numb)+","+servernumb,"The sum of the numbers is "+str(sum))
import socket
ob = socket.socket()
ob.bind(('localhost',2301))

#ob.bind(('192.168.43.97',2301))
ob.listen(4)
clintobject,add=ob.accept()
print("server ready to conect")
print("conect with this address",add)
# to recive data from client
#gotmsg = clintobject.recv(1024)
#gotmsg.decode('utf-8')
#print(gotmsg)

conn = True
while conn:
    gotmsg=clintobject.recv(1024)
    gotmsg.decode('utf-8')
    print(gotmsg)
    if len(gotmsg)==0:
        conn=False
        ob.close()
#ob.close()
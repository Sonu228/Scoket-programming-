import socket
ob = socket.socket()
ob.connect(('localhost',2301))

#msg='hello this is first client'
#send the msg
conn=True
while conn:
      msg=input("Enter you massasge")
      ob.send(msg.encode('utf-8'))
      if msg=='no':
         conn=False
         ob.close()

#ob.close()
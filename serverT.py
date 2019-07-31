#In this program:
#Create a TCP socket object
#Bind it to the host and port
#is used to connect the client to it
#Start listening on our server to receive an incomming connection from a client
#Server receives continuous stream of bytes from client, decode it
#and send that back to client using telnet
import socket
import sys

#Create Socket
#socket.AF_INET --> it's gonna take an IP4 address
#socket.SOCK_STREAM --> it's gonna be TCP oriented socket
#=======================================================
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Socket not created successfully')
    sis.exit()
print('Socket Creatred')


#Bind server socket to the host and port
#=======================================
host = '' #empty:we can listen on any interface we chose
port = 8888 #can be any number

try:
    s.bind((host, port))
except socket.error:
    print('Binding failed')
    sys.exit()
print('Socket has been bounded')


#Listen for incoming connections:
#================================
s.listen(8) #up to 8 user can be qued to handle their request and 9th qued connection is rejected be rejected
print('Socket is ready')
conn, add = s.accept() #accept incoming connection, returns two variable
print('Connected with ' + add[0] + ':' + str(add[1])) #add[0]: IP add of the connected client
                                                    #add[1]: Port of the connected client
while 1:
    data = conn.recv(1024)#1K_byte , Recieve data from client
##    decode_data = data.decode('utf-8')
    print(data.decode())
    if not data:
        break
##    conn.sendall(str.encode(decode_data))#server send data to all connected clients
                #because after we find one connection with a client we can't accept any more connection
                #so it just sends to connected client
    conn.sendall(data)
   

conn.close()#close socket connection between server and client
s.close()#close the socket which allows connection between server and client to exists






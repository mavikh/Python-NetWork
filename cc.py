import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1357 #same number as in server
s.connect((socket.gethostname(), port))

##s.send(bytes("I am connected to the server","utf-8"))
s.send(str("I am connected to the server").encode()) # send data to server

data = s.recv(1024)
s.close()

print("received data:", data)

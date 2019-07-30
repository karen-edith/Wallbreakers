# 3 client requests
import socket

client = socket.socket() # create socket object
client.connect(('localhost', 4232)) # request a connection to server socket
client.send(b'test 1') # send data through connection
print(client.recv(1024).decode()) # print recieved data
client.close() # close socket

client = socket.socket()
client.connect(('localhost', 4232))
client.send(b'test 2')
print(client.recv(1024).decode())
client.close()

client = socket.socket()
client.connect(('localhost', 4232))
client.send(b'test 3')
print(client.recv(1024).decode())
client.close()

import time
from socket import *

clientsock = socket(AF_INET,SOCK_STREAM)
clientsock.connect(('127.0.0.1',5001))

clientsock.send('Connecttttteeeeeeeeeeeeed')

print clientsock.recv(1024)
clientsock.close()

print 'Received'
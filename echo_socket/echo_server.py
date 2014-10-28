#_*_coding:utf-8_*_
#echo_server

from socket import *
import time

s=socket(AF_INET,SOCK_STREAM)
s.bind(('',8888))
s.listen(5)
while 1:
    client,addr=s.accept()
    print 'Got a connection from ',addr
    client.send(time.ctime(time.time()))
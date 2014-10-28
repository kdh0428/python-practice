#_*_coding:utf-8_*_
#echo_client

from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.connect(('127.0.0.1',8888))
tm = s.recv(1024) 
s.close()
print 'The time is ', tm
#_*_coding:utf-8_*_
#echo_client

from socket import *
s = socket(AF_INET,SOCK_STREAM) 
s.connect(('127.0.0.1',9999))
s.send("asdfasdfasdf");
s.close()

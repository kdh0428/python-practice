# Echo client program
#_*_coding:utf-8_*_
from socket import *
import thread


def hear():
    while 1:
        str = s.recv(1024)
        print str

def talk():
    while 1:
        test = raw_input(">>> ")
        s.send(test)
HOST = 'localhost'    # The remote host
PORT = 24000       # The same port as used by the server
s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST, PORT))
thread.start_new_thread(talk,())
thread.start_new_thread(hear,())
while 1: pass
s.close()

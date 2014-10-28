#_*_coding:utf-8_*_

from socket import *
import thread

def Socket_Init(PORT):
    Socket = socket(AF_INET,SOCK_STREAM)
    Socket.bind(('',PORT))
    Socket.listen(15)
    return Socket

Socket = Socket_Init(4000)

def test(conn):
    print "예아"
    while 1:
        result = conn.recv(512)
        conn.send(result)
        print result

conn,accept = Socket.accept()
thread.start_new_thread(test,(conn,))
while 1:
    pass

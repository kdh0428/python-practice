#_*_coding:utf-8_*_
from socket import *
import thread

def Init(PORT):
    Socket = socket(AF_INET,SOCK_STREAM)
    Socket.bind(('127.0.0.1',PORT))
    Socket.listen(15)
    return Socket

test = Init(40000)
test_list = []
while 1:
    conn,addr = test.accept()
    print "{} 접속".format(addr)
    test_list.append(conn)
    conn.send("잠시만 기다려주세요 ")
    conn,addr = test.accept()
    test_list.append(conn)
    
    for each in test_list:
        each.send("찾앗습니다")

    for each in test_list:
        each.close()



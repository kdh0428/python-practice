#_*_coding:utf-8_*_

from socket import *
import thread

print '##########################'
print "�ѱ� ���� ���ѹα� ����"
print '##########################'

HOST = ''
PORT = 40000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
users = []

def service():
    con, add = s.accept()
    global users
    users.append(con)
    thread.start_new_thread(service, ())
    name = con.recv(10)
    str = '***' + name + '�����˽��ϴ�'
    print users[0]
    try:
        while con:
            print str
            for each in users:
				each.send(str)
				print each.getsockname()[0]
            str = name + '] ' + con.recv(1024)
    except:
        users.remove(con)
        str = '***' + name + '�����˽��ϴ�'
        print str
        if users:
            for each in users:
                if each == 'asdfasdf' or each == '��������':
                    each.send(str)
                else:
                    pass
thread.start_new_thread(service, ())
while 1: pass

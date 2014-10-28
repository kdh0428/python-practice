from socket import *
import thread

print '##########################'
print 'asdfsadfasdfsadfsdfasfasd'
print '##########################'

HOST = '127.0.0.1'
PORT = 60000
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
    str = '***' + name + 'come'
    print users
    print type(con)
    try:
        while con:
            print str
            for each in users:
                print add[1]
                each.send(str)
                print each.sin_addr
            
            str = name + '] ' + con.recv(1024)
            print name
    except:
        users.remove(con)
        str = '***' + name + 'out'
        print str
        if users:
            for each in users:each.send(str)

thread.start_new_thread(service, ())
while 1: pass

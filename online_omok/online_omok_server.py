#_*_coding:utf-8_*_

from socket import *
import thread

print '#######################'
print 'ぞぞぞぞぞぞぞぞぞぞぞぞ'
print '#######################'

def Init(PORT):
    Socket = socket(AF_INET, SOCK_STREAM)
    Socket.bind(('',PORT))
    Socket.listen(15)
    return Socket

Game = Init(50000)
Chat = Init(40000)
Player = []

def Accept():
    global Player
    Omok_Game = Match()
    conn, addr = Game.accept()
    Player.append(conn)
    thread.start_new_thread(Accept,())


class Match(Player):
    def Battle(Player):

    def Chat(Player):
         global Player
        conn, addr = Chat.accept()
        Player.append(conn)
        name = conn.recv(10)
        str = '***' + name + 'come'
        try:
            while conn:
                print str
                for each in Player:each.send(str)
                str = name + '] ' + conn.recv(1024)
                print name
        except:
            Player.remove(conn)
            str = '***' + name + 'out'
            print str
            if Player:
                for each in Player:each.send(str)





thread.start_new_thread(Accept,())

while 1:pass

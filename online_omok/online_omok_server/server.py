#_*_coding:utf-8_*_

from socket import *
import thread
import time


def Socket_Init(PORT):
    Socket = socket(AF_INET,SOCK_STREAM)
    Socket.bind(('',PORT))
    Socket.listen(15)
    return Socket

def Omok_Game(client_conn):
    global Battle_Wait
    select = client_conn.recv(1024)
    if select == "Battle":
        Battle_Wait.append(conn)

def linker():
    global Battle_Wait
    while 1:
        if len(Battle_Wait) > 2:
            rival = [Battle.pop(0),Battle.pop(0)]
            thread.start_new_thread(Play,(rival))
        else:
            time.sleep(3)
def Play(rival):
    for each in rival:each.send("find")
    rival[0].send("select the stone")
    rival[0].recv(10)
    rival[1].send(1-rival[0])
    turn = 0
    tmp = 1
    while 1:
        check = rival[turn].recv(200)
        if check != "Finish":
            turn+=tmp
            rival[turn].send(check)
            tmp *=-1
        else:
            for each in rival:
                if rival[turn] != each:
                    each.send("Lose")
            break


Player = []
Battle_Wait = []
Game = Socket_Init(50000)
Chat = Socket_Init(40000)
if __name__ == '__main__':
    thread.start_new_thread(linker,())
    
    print '###########################'
    print '     Server is Running'
    print '###########################'
    
    while 1:
        conn,addr = Game.accept()
        print "{} 님이 접속하셧습니다.".format(addr)
        Player.append(addr[0])
        thread.start_new_thread(Omok_Game,(conn,))

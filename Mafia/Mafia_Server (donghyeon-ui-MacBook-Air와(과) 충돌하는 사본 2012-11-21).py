#_*_coding:utf-8_*_

from socket import *
import thread
import sys
import signal

def Socket_Init(PORT):
    Socket = socket(AF_INET,SOCK_STREAM)
    Socket.bind(('',PORT))
    Socket.listen(15)
    return Socket

Server_socket = Socket_Init(24000)

def check_nick(User_name,User_Nickname):
    for each in User_Nickname:
        if each == User_name:
            return -1
    return 0

def accept_player(Server_socket):
    global Player_tail
    global Player_head
    User_Nickname = []
    while 1:
        Player_conn,Player_port = Server_socket.accept()
        print Player_port
        #Player_conn.send("Test_Sucess")
        nickname = Player_conn.recv(32)
        check = check_nick(nickname,User_Nickname)
        if check<0:
            Player_conn.send('Fail\n')
            continue
        else:
            Player_conn.send('Success\n')
            User_Nickname.append(nickname)
            Player_info = Player(nickname,Player_conn)
            Player_info.next = Player_head.next
            Player_head.next = Player_info
        print "{} enter".format(nickname)


def User_Mode():
    global Player_head
    pre_player_head = Player_head
    next_node = pre_player_head.next
    while 1:
        try:
            select = pre_player_head.connect_info.recv(40)
            if select == "Quick_Search":
                str =  pre_player_head.nickname+"Quick_Search\n"
                print str
                #pre_player_head.connect_info.send(str)
                thread.start_new_thread(pre_player_head.Quick_Search,())
            elif select == "Make_Room":
                str = pre_player_head.nickname+"Make_Room\n"
                print str
                #pre_player_head.connect_info.send(str)
                thread.start_new_thread(pre_player_head.Make_Room,())
            elif select == "Refresh":
                str =  pre_player_head.nickname+"Refresh\n"
                print str
                #pre_player_head.connect_info.send(str)
                thread.start_new_thread(pre_player_head.Scan_Waiting_Room,())
            elif select.split()[0] == "Search":
                print pre_player_head.nickname+"Search "+select
                thread.start_new_thread(pre_player_head.Search,(int(select.split()[1]),))

        except:
            pass
        finally:
            pre_player_head = next_node
            next_node = next_node.next



#유저가 게임을 하면서 필요한 함수

class Player:

#유저정보

    def __init__(self, Player_nickname, Player_connect_info, next=None):
        self.nickname = Player_nickname
        self.connect_info = Player_connect_info
        self.next = next

#유저를 대기자명단으로부터 삭제

    def del_Player(self):
        global Player_head
        pre_head = Player_head
        next_head = pre_head.next
        if pre_head.nickname == self.nickname:
            Player_head = next_head
            return

        while next_head:
            if next_head.nickname == self.nickname:
                pre_head.next = next_head.next
                break
            pre_head = next_head
            next_head = next_head.next

    def add_Player(self):
        global Player_head
        self.next = Player_head.next
        Player_head.next = self

        
        
#빠른 게임 시작

    def Quick_Search(self):
        global Room_head
        if not Room_head.next.number == None:
            Min = Room_head.next.limit-Room_head.next.now
            pre_room_head = Room_head
            next_node = pre_room_head.next
            participate_room = pre_room_head
            while next_node.number !=None:
                if Min>(next_node.limit-next_node.now):
                    Min = next_node.limit-next_node.now
                    participate_room = next_node
                pre_room_head = next_node
                next_node = next_node.next
            self.connect_info.send("{0}\n{1}\n{2}\n{3}\n".format(participate_room.number,participate_room.limit,participate_room.now,participate_room.name))
        else:
            self.connect_info.send("No_Room\n")


#방 만들기

    def Make_Room(self):
        global Room_tail
        global Room_head
        self.del_Player(self.nickname)
        Room_config = Player_info.recv(512).split()
        New_Room = Room(Room_config[0],Room_config[1],Room_config[2],Room_config[3])
        New_Room.Start_Game()


        


#대기방 확인

    def Scan_Waiting_Room(self):
        global Room_head
        pre_room_head = Room_head
        next_node = pre_room_head.next
        if not next_node.number == None:
            while next_node.number != None:
                #print "{0} {1} {2} {3}\n".format(next_node.number,next_node.limit,next_node.now,next_node.name)
                self.connect_info.send("{0}\n{1}\n{2}\n{3}\n".format(next_node.number,next_node.limit,next_node.now,next_node.name))
                pre_room_head = next_node
                next_node = next_node.next
            self.connect_info.send("Finish\n")
        else:
            self.connect_info.send("No_Room\n")


    def Search(self,Room_number):
        global Room_head
        pre_room_head = Room_head
        next_node = pre_room_head.next
        if not next_node.number == None:
            while next_node.number != None:
                if Room_number == next_node.number:
                    self.connect_info.send("{0}\n{1}\n{2}\n{3}\n".format(next_node.number,next_node.limit,next_node.now,next_node.name))
                pre_room_head = next_node
                next_node = next_node.next
        else:
            self.connect_info.send("No_Room\n")

                
#------------------------------------------------------#


class Room:
    def __init__(self,Room_number,Room_limit,Room_now,Room_name,next=None):
        self.Player_head = Player(None,None)
        self.Player_tail = Player(None,None)
        self.number = Room_number
        self.name = Room_name
        self.limit = Room_limit
        self.now = Room_now
        self.next = next
        self.Player_head.next = self.Player_tail

#게임 실행시 대기방목록에서 제거
    def del_room(self):
        global Room_head
        pre_head = Room_head
        next_node = pre_head.next
        if pre_head.number == self.number:
            Room_head = next_node
            del pre_head
            return 

        while next_head:
            if next_head.number == self.number:
                pre_head.next = next_head.next
                del next_head
                break
            pre_head = next_node
            next_node = next_node.next
    def enter_room(self,Player):
        Player.del_Player()
        Player.next = self.Player_head.next
        self.Player_head.next = Player
        
    def Make_Room(self):
        global Room_head
        self.next = Room_head.next
        Room_head.next = self
        

    def out_of_room(self,Player):
        global Player_head
        pre_head = self.Player_head
        next_node = pre_head.next
        if pre_head.nickname == self.nickname:
            self.Player.next = next_node
            return

        while next_node.nickname:
            if pre_head.nickname == self.Player.nickname:
                pre_head.next = next_head.next
                break
            pre_head = next_node
            next_node = next_node.next

    def Start_Game(self):
        pre_head = self.Player_head
        next_node = pre_head.next
        while 1:
            try:
                chat = pre_head.connect_info.recv(32).split()
                if chat[0] == "Game_Start":
                    Game = Game(self.Player_head)
                    Game.Start_Game()
                else :
                    for each in self.Player_head:
                        self.Player_head.connect_info.send(pre_head.nickname+" >>"+chat[1])
            except:
                pass
            finally:
                pre_head = next_node
                next_node = next_node.next

                


        


class Game:
    
    def __init__(self,NumberofMapia=1,Player=None):
        self.date = 1
        self.NumberofMapia = NumberofMapia
        self.AliveList = []
        self.MapiaList = []
        self.DeadList = []
        self.Player_head = Player

    def Chat(self,Target):
        while len(self.AliveList)-2*(len(self.MapiaList))>0:
            try:
                chat = pre_player_head.connect_info.recv(1024).sqilt()
                if chat[0] == "Alive":
                    for each in AliveList:
                        each.send(pre_player_head.nickname+" >> "+chat[1])
                elif chat[0] == "Mapia":
                    for each in MapiaList:
                        each.send(pre_player_head.nickname+" >> "+chat[1])
                elif chat[0] == "Dead":
                    for each in DeadList:
                        each.send(pre_player_head.nickname+" >> "+chat[1])

            except:
                pre_player_head = next_node
                next_node = next_node.next

    def vote(self):
        pass
    def Start_Game(self,Gamers,Room):
        pre_player_head = Gamers
        next_node = pre_player_head.next
        while pre_player_head:
            self.AliveList.append((pre_player_head.nickname,
                pre_player_head.connect_info))
            pre_player_head = next_node
            next_node = next_node.next
        self.Mapia_Choose()

    def Mapia_Choose(self):
        while self.NumberofMapia:
            index = random.randomrange(Room.number)
            self.MapiaList.append(self.AliveList[index])
            self.NumberofMapia-=1

Player_head = Player(None,None)
Player_tail = Player(None,None)
Player_head.next = Player_tail
Player_tail.next = Player_head
Room_head = Room(None,None,None,None)
Room_test = Room(1,5,3,"덤벼라 시바")
Room_test2 = Room(2,5,4,"rerere")
Room_tail = Room(None,None,None,None)
Room_head.next = Room_test
Room_test.next = Room_test2
Room_test2.next = Room_tail
Room_tail.next = Room_head
print '#'*25
print "#Mapia_Server_Is_Running#"
print '#'*25
thread.start_new_thread(User_Mode,())
accept_player(Server_socket)


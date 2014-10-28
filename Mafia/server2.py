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

User_Select={
    "QuickSearch":Quick_Search,
    "MakeRoom":Make_Room,
    "Refresh":Scan_Waiting_Room
    }

def check_nick(nickname):
    global Player_head
        pre_player_head = Player_head
        next_node = pre_player_head.next
        while pre_player_head:
            if nickname==pre_player_head.nickname:
                return -1
            pre_player_head = next_node
            next_node = next_node.next

    
def accept_player(Server_socket):
    global Player_tail
    global Player_head
    while 1:
        Player_conn,Player_port = Server_socket.accept()
        nickname = Player_conn.recv(32)
        print "{} enter".format(nickname)
        check = check_nick(nickname)
        if check<0:
            Player_conn.send(-1)
            continue
        Player_info = Player(nickname,Player_conn)
        if Player_head.next ==None:Player_tail = Player_info
        else:
            Player_tail.next = Player_info
            Player_info.next = None

 #TDM구현을 위한 ExCeption 
class TimeoutException(Exception):
    pass
class cls_time_out_handler:
    def time_out_handler(self,signum,frame):
        raise TimeoutException()

class User_Mode(cls_timeout_handler):           
    
    def User_Mode(self):
    global Player_head
    pre_player_head = Player_head
    next_node = pre_player_head.next
    signal.signal(signal.SIGALRM,timeout_handler)
    while 1:
        try:
            signal.setitimer(signal.ITIMER_REAL,0.1)
            select = pre_player_head.connect_info.recv(40)
            signal.alarm(0)
            thread.start_new_thread((pre_player_head.User_Select.get(select)()),())
        except:
            pre_player_head = next_node
            next_node = next_node.next
            signal.alarm(0)



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
        pre_head = head
        next_node = pre_head.next
        if pre_head == self.nickname:
            head = next_node
            del pre_head
            return 

        while next_head:
            if next_head.nickname == self.nickname:
                pre_head.next = next_head.next
                del next_head
                break
            pre_head = next_node
            next_node = next_node.next

#빠른 게임 시작

    def Quick_Search(self):
        global Room_head
        Max = Room_head.next.limit-Room_head.next.now
        pre_room_head = Room_head
        next_node = pre_room_head.next
        while pre_room_head:
            if Max<(pre_room_head.limit-pre_room_head.now):
                Max = pre_room_head.limit-pre_room_head.now
            pre_room_head = next_node
            next_node = next_node.next

        


#대기방 확인

    def Scan_Waiting_Room(self):
        global Room_head
        pre_room_head = Room_head
        next_node = pre_room_head.next
        while pre_room_head:
            self.connect_info.send("") #주어야할 값들
            pre_room_head = next_node
            next_node = next_node.next
                
#------------------------------------------------------#


class Room:
    def __init__(self,Room_number,Room_name,Room_limit,Room_now,next=None):
        self.number = Room_number
        self.name = Room_name
        self.limit = Room_limit
        self.now = Room_now
        self.next = next

#게임 실행시 대기방목록에서 제거
    def del_room(self):
        global Room_head
        pre_head = Room_head
        next_node = pre_head.next
        if pre_head == self.number:
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

#방 만들기

    def Make_Room(self,Player_info):
        global Room_tail
        global Room_head
        Player_info.del_Player(Player_info.nickname)
        Room_config = Player_info.recv(512).split()

        self.number = Room_config[]
        self.name = Room_config[]
        self.limit = Room_config[]
        self.now = Room_config[]

    if Room_head.next==None: Room_tail = self
    else:
        Room_tail.next = self
        self.next = None

class Game(cls_time_out_handler):
    
    def __init__(self,NumberofMapia=1):
        self.date = 1
        self.NumberofMapia = NumberofMapia
        self.AliveList = []
        self.MapiaList = []
        self.DeadList = []

    def Chat(self,Target):
        signal.signal(signal.SIGALRM,timeout_handler)
        while len(self.AliveList)-2*(len(self.MapiaList))>0:
            try:
                signal.setitimer(signal.ITIMER_REAL,0.1)
                select = pre_player_head.connect_info.recv(1024)
                if select = "Alivie":
                signal.alarm(0)
                thread.start_new_thread((pre_player_head.User_Select.get(select)()),())
            except:
                pre_player_head = next_node
                next_node = next_node.next
                signal.alarm(0)

            


        
        
        

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
Room_head = Room(None,None,None,None)
Room_tail = Room(None,None,None,None)



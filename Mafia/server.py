#_*_coding:utf-8_*_

from socket import *
import thread
import sys
import signal
class Player_info:
    def __init__(self, Player_nickname, Player_connect_info, next=None):
        self.nickname = Player_nickname
        self.connect_info = Player_connect_info
        self.next = next
    def del_Player(self,del_Player_nickname):
        global Player_head
        pre_head = head
        next_node = pre_head.next
        if pre_head == del_Player_nickname:
            head = next_node
            del pre_head
            return 

        while next_head:
            if next_head.data == del_Player_nickname:
                pre_head.next = next_head.next
                del next_head
                break
            pre_head = next_node
            next_node = next_node.next


    def add_node(self,add_node_Player_nickname):
        pass


class Room_info:
    def __init__(self,Room_number,Room_name,Room_limit,Room_now,next=None):
        self.number = Room_number
        self.name = Room_name
        self.limit = Room_limit
        self.now = Room_now
        self.next = next
    
    def del_room(self,del_room_number):
        global Room_head
        pre_head = head
        next_node = pre_head.next
        if pre_head == del_room_number:
            head = next_node
            del pre_head
            return 

        while next_head:
            if next_head.data == del_room_number:
                pre_head.next = next_head.next
                del next_head
                break
            pre_head = next_node
            next_node = next_node.next



Player_head = Player_info(None,None)
Player_tail = Player_info(None,None)
Room_head = Room_info(None,None,None,None)
Room_tail = Room_info(None,None,None,None)
Player_head.next = Player_tail
Room_head.next = Room_tail.next
class TimeoutException(Exception):
    pass
def Socket_Init(PORT):
    Socket = socket(AF_INET,SOCK_STREAM)
    Socket.bind(('',PORT))
    Socket.listen(15)
    return Socket

def accept_player(Server_socket):
    while 1:
        Player_conn,Player_port = Server_socket.accept()
        nickname = Player_conn.recv(32)
        Player = Player_info(nickname,Player_conn)
        tail = Player
        tail.next = None




def time_out_handler(signum,frame):
        raise TimeoutException()

def Waiting_Room():
    global Room_head
    global Player_head
    pre_room_head = Room_head
    pre_player_head = Player_head
    signal.signal(signal.SIGALRM,timeout_handler)
    try:
        signal.setitimer(signal.ITIMER_REAL,0.1)
        pre_player_head.recv(40)
        signal.alarm(0)
        while pre_room_head:
            recv.send("") #주어야할 값들
            pre_room_head = pre_room_head.next

    except:
        pre_player_head = pre_player_head.next
        signal.alarm(0)


            

        

#    def Waiting_Person(self):
#        signal.signal(signal.SIGALRM, timeout_handler)
#        try:
#            signal.setitimer(signal.ITIMER_REAL,0.1)
#            self.head.connect_info.recv(32)
#        except TimeoutException:
#           self.head = self.head.next
        

Server_socket=Socket_Init(24000)
thread.start_new_thread(accept_player,(Server_socket,))
thread.start_new_thread(Waiting_Room,())
while 1: pass


#_*_coding:utf-8_*_

from socket import *
from Tkinter import *

color = ["black","white"];

before = now = 0;
root = Tk()
board = Canvas(root,width=482,height=482,bg="#FFC800")
def draw_board():
    for i in range(30):
        board.create_line(0,30*i+3,482,30*i+3,fill='black',width=2)
        board.create_line(30*i+3,0,30*i+3,484,fill='black',width=2)
    board.pack()
class Battle():
    fight = 0
    def round_off(self,num):
        num = (num+15)/30 * 30
        return num+2

    def put_before(self,event):
        global before,now;
        board.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,width=0,fill=color[before])
        print before,now;
        before+=now;
        now+=1;
    def put(self,event):
        global before,now;
        if self.fight:
            self.put_before(self.event_before)
            now -= 2*before;
        event.x = self.round_off(event.x)
        event.y = self.round_off(event.y)
        board.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,width=0,fill=color[now])
        board.create_oval(event.x-3,event.y-3,event.x+4,event.y+4,width=0,fill="red")
        self.event_before = event
        self.fight = 1
        print "clicked at",event.x,event.y
    def start(self):
        board.bind("<Button-1>",self.put)
draw_board()
test = Battle()
test.start()
root.mainloop()

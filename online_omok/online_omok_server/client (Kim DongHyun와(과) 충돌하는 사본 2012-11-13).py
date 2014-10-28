#_*_coding:utf-8_*_

from socket import *
from Tkinter import *
import Image,ImageTk


root = Tk()
def draw_board():
    v = Canvas(root,width=482,height=484,bg="#FFC81E")
    for i in range(30):
        v.create_line(0,30*i+4,506,30*i+4,fill='black',width=2)
        v.create_line(30*i+4,0,30*i+4,484,fill='black',width=2)
    v.pack()

class Battle:
    global root
    global stone
    def round_off(self,num):
        if num%30>=15:
         num +=30-(num%30)
        else:
           num -=(num%30)
        return num

    def put(self,event):
        
        print "clicked at",event.x,event.y

    def start(self):
        pass

test = Battle()
test.start()
draw_board()
root.mainloop()

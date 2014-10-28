#_*_coding:utf-8_*_

from socket import *
from Tkinter import *

import tkSimpleDialog, thread

def talk(event):
    s.send(ent.get())
    ent.delete(0, END)

def hear():
    while 1:
        str = s.recv(1024) + '\n'
        str = unicode(str)
        txt.config(state=NORMAL)
        txt.insert(END, str)
        txt.config(state=DISABLED)
        ent.focus()
root = Tk()
root.title('HM CHAT ROOM')
ent = Entry(root)
ent.pack(fill=X)
ent.insert(0, '')
ent.bind('<Return>', talk)
txt = Text(root)
txt.pack()
name = tkSimpleDialog.askstring('CHAT ROOM',
            unicode('Pls input your name'))
if name:
    HOST = '127.0.0.1'
    PORT = 40000
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(name)
    thread.start_new_thread(hear, ())
    mainloop()

#_*_coding:utf-8_*_
from Tkinter import *

root = Tk()
v = Canvas(root,width=482,height=484,bg='#FFC81E')
for i in range(30):
    v.create_line(0,30*i+4,506,30*i+4,fill='black',width=2)
    v.create_line(30*i+4,0,30*i+4,484,fill='black',width=2)
v.pack()
root.mainloop()

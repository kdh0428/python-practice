from Tkinter import *
import Image,ImageTk

root = Tk()
minlabel = Label()
minlabel.image = ImageTk.PhotoImage(Image.open("./Image/Omok_Board.png"))

minlabel.pack()
root.mainloop()
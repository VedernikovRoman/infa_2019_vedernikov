from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
text = StringVar()
label = Label(root, textvariable=text, fg = "#eee", bg = "#333")
label.pack()
colors = ['red','orange','yellow','green','blue']




def new_ball():
    global x,y,r, krug1, x1, y1, r1, krug2
    canv.delete(ALL)
    x = rnd(100,600)
    y = rnd(100,400)
    r = rnd(20,50)
    krug1 = canv.create_oval(x - r,y - r,x + r,y + r, fill = choice(colors), width=0)
    x1 = rnd(100,600)
    y1 = rnd(100,400)
    r1 = rnd(20,50)
    krug2 = canv.create_oval(x1 - r1,y1 - r1,x1 + r1,y1 + r1, fill = choice(colors), width=0)
    x2 = rnd(100,600)
    y2 = rnd(100,400)
    r2 = rnd(30,80)

def click(event):
    global n
    if (event.x - x1)**2+(event.y - y1)**2 < r1**2:
        n += 1
        print("Vnature 4otko")
        print(n)
    elif (event.x - x)**2+(event.y - y)**2 < r**2:
        n += 1
        print("zaebis")
        print(n)
    else:
        print ("opushen")
        
    text.set(str(n))
        
def update():
    global dx,dy,x,y,r, krug1
    global dx1,dy1,x1,y1,r1, krug2
    global n
    
    x += dx
    y += dy
    if x <= r:
        dx = rnd(1,10)
        dy = rnd(-10,10)
    if x >= 800-r:
        dx = -rnd(1,10)
        dy = rnd(-10,10)
    if y >= 600-r:
        dy = -rnd(1,10)
        dx = rnd(-10,10)
    if y <= r:
        dy = rnd(1,10)
        dx = rnd(-10,10)
    canv.move(krug1,dx,dy)
    
    x1 += dx1
    y1 += dy1
    if x1 <= r1:
        dx1 = rnd(1,10)
        dy1 = rnd(-10,10)
    if x1 >= 800-r1:
        dx1 = -rnd(1,10)
        dy1 = rnd(-10,10)
    if y1 >= 600-r1:
        dy1 = -rnd(1,10)
        dx1 = rnd(-10,10)
    if y1 <= r1:
        dy1 = rnd(1,10)
        dx1 = rnd(-10,10)
    canv.move(krug2,dx1,dy1)
    root.after(50, update)





def igra():
    global dy,dx,x,y,r,dy1,dx1,x1,y1,r1
    dx = rnd(1,5)
    dy = rnd(1,5)
    dx1 = rnd(1,5)
    dy1 = rnd(1,5)
    new_ball()
    update()
    root.after(10000,igra)

n = 0
igra()
canv.bind('<Button-1>', click)

mainloop()
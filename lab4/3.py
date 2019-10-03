
from graph import *
from math import *
import math as m
a = []
windowSize(800, 400)
canvasSize(800, 400)

penColor(0, 0, 0)
brushColor(14, 147, 37)
rectangle(0, 225, 800, 400) #grass

brushColor(153, 227, 237)
rectangle(0, 0, 800, 225)# sky


def house(x,y,m): #x=100 y=200
    penColor("black")
    brushColor(147, 107, 14)
    rectangle(x*m, y*m, (x+100)*m, (y+100)*m)#house1

    brushColor(235, 47, 68)
    polygon([(x*m,y*m), ((x+50)*m,(y-50)*m),
         ((x+100)*m,y*m), (x*m,y*m)])
    penColor("white")#window1

    brushColor(14, 147, 145)
    rectangle((x+27)*6, (y+25)*6, (x+72)*6, (y+60)*6)
    penColor(0,0,0)#roof

    penColor("black")
    brushColor("brown")
    rectangle((x+34)*m, (y+25)*m, (x+66)*m, (y+100)*m)
    
    penColor("white")
    brushColor(14, 147, 229)
    rectangle((x+5)*m, (y+40)*m, (x+30)*m, (y+65)*m) 
    rectangle((x+70)*m, (y+40)*m, (x+95)*m, (y+65)*m)
    
def cloud(x,y): #x 150 y 90
    brushColor("white")
    circle(x, y-20, 25)
    circle(x+30, y-20, 25)
    circle(x+60, y-20, 25)
    circle(x-15, y, 25)
    circle(x+15, y, 25)
    circle(x+45, y, 25)
    circle(x+75, y, 25)
    brushColor(0, 0, 0)
    
house(100,200,1)
house(400,230,0.8)
house(860,250,0.7)
cloud(150,90)
cloud(400,60)
cloud(600,100)



penColor(0, 0,0)
rectangle(280, 175,295, 275)
brushColor(15, 83, 14)
penColor(0, 0, 0)
circle(290, 110, 30)
circle(262, 130, 30)
circle(308, 130, 30)
circle(290, 150, 30)
circle(262, 170, 30)
circle(308, 170, 30)
brushColor("orange")# sun

penColor("orange")
n = 45
for i in range(n):
    x = 65
    y = 60
    if i%2 == 0:
        a.append((x+30*m.cos(2*m.pi*i/n), y+30*m.sin(2*m.pi*i/n)))
    else:
        a.append((x+35*m.cos(2*m.pi*i/n), y+35*m.sin(2*m.pi*i/n)))
polygon(a)





run()

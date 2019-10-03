
from graph import *
windowSize(800, 400)
canvasSize(800, 400)

penColor(0, 0, 0)
brushColor(52, 255, 68)
rectangle(0, 225, 800, 400)
brushColor(126, 172, 242)
rectangle(0, 0, 800, 225)

def house(x,y): 
    penColor("black")
    brushColor(217, 142, 2)
    rectangle(x, y, x+100, y+100)
    brushColor(229, 14, 89)
    polygon([(x,y), (x+50,y-75),
         (x+100,y), (x,y)])
    
    brushColor("brown")
    rectangle(x+34, y+25, x+66, y+100)
    
    penColor("white")
    brushColor(14, 147, 229)
    rectangle(x+5, y+40, x+30, y+65) 
    rectangle(x+70, y+40, x+95, y+65) 
    
    penColor("black")
    brushColor("black")    
    circle(x+60, y+60, 3)
    
    
    

house(100,200)
house(330,220)
house(570,180)

penColor(0,0,0)
brushColor("white")
circle(300, 50, 25)
circle(330, 50, 25)
circle(270, 80, 25)
circle(300, 80, 25)
circle(330, 80, 25)
circle(360, 80, 25)
brushColor(28, 17, 1)
rectangle(500, 175,515, 275)
brushColor(12, 69, 19)
circle(510, 100, 30)
circle(535, 120, 30)
circle(480, 120, 30)
circle(510, 140, 30)
circle(535, 160, 30)
circle(480, 160, 30)



run()

from graph import *

def chaika(x0,y0,a):
    penColor("white")
    penSize(3)
    moveTo(x0, y0)
    b = x0
    c = y0
    x = x0
    y = y0
    for i in range(a):
        x += 1
        y -= ((i + 1)**0.5 - i ** 0.5)*3
        lineTo(x,y)
        x0, y0 = x, y
    x0 = b
    y0 = c
    x = x0
    y = y0 
    moveTo(x0, y0)
    for i in range(a):
        x -= 1
        y -= ((i + 1)**0.5 - i ** 0.5)*3
        lineTo(x,y)
        x0, y0 = x, y      
        
def ellipse(x1,y1,x2,y2,r):
    for i in range (460):
        for j in range(650):
            module1=((x1-i)**2+(y1-j)**2)**0.5
            module2=((x2-i)**2+(y2-j)**2)**0.5
            if ((module1+module2)<r) :
                point(i,j)

def ryba(x1,y1,x2,y2,s,t):
    penColor("orange")
    penSize(1)
    brushColor("orange")
    polygon([(360-s,560-t),(340-s,535-t),(380-s,540-t),(380-s,560-t)])  
    
    penColor("darkcyan")
    penSize(1)
    brushColor("darkcyan")
    
    for i in range (460):
        for j in range(650):    
            a=((x1-s-i)**2+(y1-t-j)**2)**0.5
            b=((x2-s-i)**2+(y2-t-j)**2)**0.5 
            if ((a<80) and (b<80)):
                point(i,j)
                polygon([(325-s,565-t),(305-s,580-t),(310-s,565-t),(305-s,550-t)])
                
    penColor("blue")
    penSize(1)
    brushColor("blue")
    circle(390-s,565-t, 7)
    
    
    penColor("black")
    penSize(1)
    brushColor("black")
    circle(393-s,565-t, 3)    
    
    
    
    


brushColor("navy")
rectangle(0,650,460,280)

brushColor("red")
penColor("red")
rectangle(0,40,460,0)

brushColor("orange")
penColor("orange")
rectangle(0,80,460,40)

brushColor("yellow")
penColor("yellow")
rectangle(0,120,460,80)

brushColor("green")
penColor("green")
rectangle(0,160,460,120)

brushColor("aqua")
penColor("aqua")
rectangle(0,200,460,160)

brushColor("blue")
penColor("blue")
rectangle(0,240,460,200)

brushColor("purple")
penColor("purple")
rectangle(0,280,460,240)

chaika(100,60,50)
chaika(300,100,70)
chaika(150,160,40)

penColor("black")
penSize(1)
brushColor("yellow")
u=17
polygon([(380,437),(410,440),(420,430),(410,430),(390,430),(380,427)])
polygon([(380,427),(390,430),(410,430),(420,430),(413,424)])
polygon([(295,530),(295,550),(300,535),(320,540),(305,530),(325,535),(310,525),(325,525),(317,520),(290,525)])
polygon([(295-u,530+u),(295-u,550+u),(300-u,535+u),(320-u,540+u),(305-u,530+u),(325-u,535+u),(310-u,525+u),(325-u,525+u),(317-u,520+u),(290-u,525+u)])

penColor("white")
penSize(1)
brushColor("white")

ellipse(290,450,345,450, 65)
ellipse(335,435,380,435, 55)
ellipse(200,490,240,530, 65)
ellipse(220,475,260,515, 65)
ellipse(230,537,280,547, 53)
ellipse(245,520,295,530, 53)

penColor("black")
penSize(1)
brushColor("white")
polygon([(150,470), (130,468), (90,460), (100, 400), (150,450)]) 

polygon([(220,440), (220,400), (210,360), (205,350),(90,340),(70,330),(90,360),(140,370),(200,440) ])

polygon([(160,440), (130,420), (110,400), (60, 390), (40,360),(60,370),(130,375),(180,375),(185,380),(200,475) ])



penColor("white")
penSize(1)
brushColor("white")
ellipse(150,460,300,460, 170)

penColor("black")
penSize(1)
brushColor("black")
ellipse(365,430,375,430, 12)



ryba(370, 500,370,630,0,0)

penColor("blue")
penSize(1)
brushColor("blue")
circle(390,565, 7)

penColor("black")
penSize(1)
brushColor("black")
circle(393,565, 3)
run()
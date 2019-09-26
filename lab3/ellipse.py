from graph import *
import numpy

def ellipse_dot(t, a, b,x,y,f):
    return a*cos(t)*cos(f) + b*sin(t)*sin(f) + x, -a*cos(t)*sin(f) + b*sin(t)*cos(f) + y

def ellipse(a,b,x,y,f):
    points = [ellipse_dot(t, a, b,x,y,f) for t in numpy.linspace(0, 2*pi, num=100)]
    return points

def gtr(f):
    return f/180*pi
from math import sin, cos, pi, sqrt
brushColor("red")
polygon(ellipse(150,100,200,300,gtr(30)))